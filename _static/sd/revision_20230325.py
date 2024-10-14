# Author: XpucT
# Script's homepage: https://boosty.to/xpuct

import modules.scripts as scripts
import gradio as gr
import numpy as np
import cv2
import math

from PIL import Image
from modules.processing import process_images, Processed
from PIL import ImageEnhance, Image, ImageDraw, ImageFilter, ImageChops, ImageOps
from blendmodes.blend import blendLayers, BlendType
from typing import List


def add_chromatic(im, strength: float = 1, no_blur: bool = False):

    if (im.size[0] % 2 == 0 or im.size[1] % 2 == 0):
        if (im.size[0] % 2 == 0):
            im = im.crop((0, 0, im.size[0] - 1, im.size[1]))
            im.load()
        if (im.size[1] % 2 == 0):
            im = im.crop((0, 0, im.size[0], im.size[1] - 1))
            im.load()

    def cartesian_to_polar(data: np.ndarray) -> np.ndarray:
        width = data.shape[1]
        height = data.shape[0]
        assert (width > 2)
        assert (height > 2)
        assert (width % 2 == 1)
        assert (height % 2 == 1)
        perimeter = 2 * (width + height - 2)
        halfdiag = math.ceil(((width ** 2 + height ** 2) ** 0.5) / 2)
        halfw = width // 2
        halfh = height // 2
        ret = np.zeros((halfdiag, perimeter, 3))

        ret[0:(halfw + 1), halfh] = data[halfh, halfw::-1]
        ret[0:(halfw + 1), height + width - 2 +
            halfh] = data[halfh, halfw:(halfw * 2 + 1)]
        ret[0:(halfh + 1), height - 1 +
            halfw] = data[halfh:(halfh * 2 + 1), halfw]
        ret[0:(halfh + 1), perimeter - halfw] = data[halfh::-1, halfw]

        for i in range(0, halfh):
            slope = (halfh - i) / (halfw)
            diagx = ((halfdiag ** 2) / (slope ** 2 + 1)) ** 0.5
            unit_xstep = diagx / (halfdiag - 1)
            unit_ystep = diagx * slope / (halfdiag - 1)
            for row in range(halfdiag):
                ystep = round(row * unit_ystep)
                xstep = round(row * unit_xstep)
                if ((halfh >= ystep) and halfw >= xstep):
                    ret[row, i] = data[halfh - ystep, halfw - xstep]
                    ret[row, height - 1 - i] = data[halfh + ystep, halfw - xstep]
                    ret[row, height + width - 2 +
                        i] = data[halfh + ystep, halfw + xstep]
                    ret[row, height + width + height - 3 -
                        i] = data[halfh - ystep, halfw + xstep]
                else:
                    break

        for j in range(1, halfw):
            slope = (halfh) / (halfw - j)
            diagx = ((halfdiag ** 2) / (slope ** 2 + 1)) ** 0.5
            unit_xstep = diagx / (halfdiag - 1)
            unit_ystep = diagx * slope / (halfdiag - 1)
            for row in range(halfdiag):
                ystep = round(row * unit_ystep)
                xstep = round(row * unit_xstep)
                if (halfw >= xstep and halfh >= ystep):
                    ret[row, height - 1 + j] = data[halfh + ystep, halfw - xstep]
                    ret[row, height + width - 2 -
                        j] = data[halfh + ystep, halfw + xstep]
                    ret[row, height + width + height - 3 +
                        j] = data[halfh - ystep, halfw + xstep]
                    ret[row, perimeter - j] = data[halfh - ystep, halfw - xstep]
                else:
                    break
        return ret

    def polar_to_cartesian(data: np.ndarray, width: int, height: int) -> np.ndarray:
        assert (width > 2)
        assert (height > 2)
        assert (width % 2 == 1)
        assert (height % 2 == 1)
        perimeter = 2 * (width + height - 2)
        halfdiag = math.ceil(((width ** 2 + height ** 2) ** 0.5) / 2)
        halfw = width // 2
        halfh = height // 2
        ret = np.zeros((height, width, 3))

        def div0():
            ret[halfh, halfw::-1] = data[0:(halfw + 1), halfh]
            ret[halfh, halfw:(halfw * 2 + 1)] = data[0:(halfw + 1),
                                                     height + width - 2 + halfh]
            ret[halfh:(halfh * 2 + 1), halfw] = data[0:(halfh + 1),
                                                     height - 1 + halfw]
            ret[halfh::-1, halfw] = data[0:(halfh + 1), perimeter - halfw]

        div0()

        def part1():
            for i in range(0, halfh):
                slope = (halfh - i) / (halfw)
                diagx = ((halfdiag ** 2) / (slope ** 2 + 1)) ** 0.5
                unit_xstep = diagx / (halfdiag - 1)
                unit_ystep = diagx * slope / (halfdiag - 1)
                for row in range(halfdiag):
                    ystep = round(row * unit_ystep)
                    xstep = round(row * unit_xstep)
                    if ((halfh >= ystep) and halfw >= xstep):
                        ret[halfh - ystep, halfw - xstep] = \
                            data[row, i]
                        ret[halfh + ystep, halfw - xstep] = \
                            data[row, height - 1 - i]
                        ret[halfh + ystep, halfw + xstep] = \
                            data[row, height + width - 2 + i]
                        ret[halfh - ystep, halfw + xstep] = \
                            data[row, height + width + height - 3 - i]
                    else:
                        break

        part1()

        def part2():
            for j in range(1, halfw):
                slope = (halfh) / (halfw - j)
                diagx = ((halfdiag ** 2) / (slope ** 2 + 1)) ** 0.5
                unit_xstep = diagx / (halfdiag - 1)
                unit_ystep = diagx * slope / (halfdiag - 1)
                for row in range(halfdiag):
                    ystep = round(row * unit_ystep)
                    xstep = round(row * unit_xstep)
                    if (halfw >= xstep and halfh >= ystep):
                        ret[halfh + ystep, halfw - xstep] = \
                            data[row, height - 1 + j]
                        ret[halfh + ystep, halfw + xstep] = \
                            data[row, height + width - 2 - j]
                        ret[halfh - ystep, halfw + xstep] = \
                            data[row, height + width + height - 3 + j]
                        ret[halfh - ystep, halfw - xstep] = \
                            data[row, perimeter - j]
                    else:
                        break

        part2()

        def set_zeros():
            zero_mask = ret[1:-1, 1:-1] == 0
            ret[1:-1, 1:-1] = np.where(zero_mask, (ret[:-2,
                                                       1:-1] + ret[2:, 1:-1]) / 2, ret[1:-1, 1:-1])

        set_zeros()

        return ret

    def get_gauss(n: int) -> List[float]:
        sigma = 0.3 * (n / 2 - 1) + 0.8
        r = range(-int(n / 2), int(n / 2) + 1)
        new_sum = sum([1 / (sigma * math.sqrt(2 * math.pi)) *
                       math.exp(-float(x) ** 2 / (2 * sigma ** 2)) for x in r])
        return [(1 / (sigma * math.sqrt(2 * math.pi)) *
                math.exp(-float(x) ** 2 / (2 * sigma ** 2))) / new_sum for x in r]

    def vertical_gaussian(data: np.ndarray, n: int) -> np.ndarray:
        padding = n - 1
        width = data.shape[1]
        height = data.shape[0]
        padded_data = np.zeros((height + padding * 2, width))
        padded_data[padding: -padding, :] = data
        ret = np.zeros((height, width))
        kernel = None
        old_radius = - 1
        for i in range(height):
            radius = round(i * padding / (height - 1)) + 1
            if (radius != old_radius):
                old_radius = radius
                kernel = np.tile(get_gauss(1 + 2 * (radius - 1)),
                                 (width, 1)).transpose()
            ret[i, :] = np.sum(np.multiply(
                padded_data[padding + i - radius + 1:padding + i + radius, :], kernel), axis=0)
        return ret

    r, g, b = im.split()
    rdata = np.asarray(r)
    gdata = np.asarray(g)
    bdata = np.asarray(b)
    if no_blur:
        rfinal = r
        gfinal = g
        bfinal = b
    else:
        poles = cartesian_to_polar(np.stack([rdata, gdata, bdata], axis=-1))
        rpolar, gpolar, bpolar = poles[:, :,
                                       0], poles[:, :, 1], poles[:, :, 2],

        bluramount = (im.size[0] + im.size[1] - 2) / 100 * strength
        if round(bluramount) > 0:
            rpolar = vertical_gaussian(rpolar, round(bluramount))
            gpolar = vertical_gaussian(gpolar, round(bluramount * 1.2))
            bpolar = vertical_gaussian(bpolar, round(bluramount * 1.4))

        rgbpolar = np.stack([rpolar, gpolar, bpolar], axis=-1)
        cartes = polar_to_cartesian(
            rgbpolar, width=rdata.shape[1], height=rdata.shape[0])
        rcartes, gcartes, bcartes = cartes[:, :,
                                           0], cartes[:, :, 1], cartes[:, :, 2],

        rfinal = Image.fromarray(np.uint8(rcartes), 'L')
        gfinal = Image.fromarray(np.uint8(gcartes), 'L')
        bfinal = Image.fromarray(np.uint8(bcartes), 'L')

    gfinal = gfinal.resize((round((1 + 0.018 * strength) * rdata.shape[1]),
                            round((1 + 0.018 * strength) * rdata.shape[0])), Image.ANTIALIAS)
    bfinal = bfinal.resize((round((1 + 0.044 * strength) * rdata.shape[1]),
                            round((1 + 0.044 * strength) * rdata.shape[0])), Image.ANTIALIAS)

    rwidth, rheight = rfinal.size
    gwidth, gheight = gfinal.size
    bwidth, bheight = bfinal.size
    rhdiff = (bheight - rheight) // 2
    rwdiff = (bwidth - rwidth) // 2
    ghdiff = (bheight - gheight) // 2
    gwdiff = (bwidth - gwidth) // 2

    im = Image.merge("RGB", (
        rfinal.crop((-rwdiff, -rhdiff, bwidth - rwdiff, bheight - rhdiff)),
        gfinal.crop((-gwdiff, -ghdiff, bwidth - gwdiff, bheight - ghdiff)),
        bfinal))

    return im.crop((rwdiff, rhdiff, rwidth + rwdiff, rheight + rhdiff))


def resetValues(saturationSlider, temperatureSlider, brightnessSlider, contrastSlider, sharpnessSlider, blurSlider, noiseSlider, vignetteSlider, exposureOffsetSlider, hdrSlider):
    saturationSlider = 1
    temperatureSlider = 1
    brightnessSlider = 1
    contrastSlider = 1
    sharpnessSlider = 0
    blurSlider = 0
    noiseSlider = 0
    vignetteSlider = 0
    exposureOffsetSlider = 0
    hdrSlider = 0
    return [saturationSlider, temperatureSlider, brightnessSlider, contrastSlider, sharpnessSlider, blurSlider, noiseSlider, vignetteSlider, exposureOffsetSlider, hdrSlider]


def bestChoiceValues(saturationSlider, temperatureSlider, brightnessSlider, contrastSlider, sharpnessSlider, blurSlider, noiseSlider, vignetteSlider, exposureOffsetSlider, hdrSlider):
    saturationSlider = .98
    temperatureSlider = 1.04
    brightnessSlider = 1.01
    contrastSlider = .97
    sharpnessSlider = .02
    blurSlider = 0
    noiseSlider = .03
    vignetteSlider = .05
    exposureOffsetSlider = .1
    hdrSlider = .16
    return [saturationSlider, temperatureSlider, brightnessSlider, contrastSlider, sharpnessSlider, blurSlider, noiseSlider, vignetteSlider, exposureOffsetSlider, hdrSlider]


class Script(scripts.Script):
    def title(self):
        return 'Revision'

    def show(self, is_img2img):
        return scripts.AlwaysVisible

    def ui(self, is_img2img):
        with gr.Accordion('Revision', open=False):
            with gr.Tab(label='Options', id=1):
                enabled = gr.Checkbox(label="Enable")
                clearEXIFCheckbox = gr.Checkbox(
                    label="Clear EXIF (all metadata)")
                flipImageCheckbox = gr.Checkbox(label="Flip image")
                dontShowOriginalCheckbox = gr.Checkbox(
                    label="Don't show original image")

            with gr.Tab(label='Adjustments', id=2):
                saturationSlider = gr.Slider(0, 2, 1, label='Saturation')
                temperatureSlider = gr.Slider(0, 2, 1, label='Temperature')
                brightnessSlider = gr.Slider(0, 2, 1, label='Brightness')
                contrastSlider = gr.Slider(0, 2, 1, label='Contrast')
                sharpnessSlider = gr.Slider(0, 1, 0, label='Sharpness')
                blurSlider = gr.Slider(0, 1, 0, label='Blur')
                noiseSlider = gr.Slider(0, 1, 0, label='Noise')
                vignetteSlider = gr.Slider(0, 1, 0, step=.05, label='Vignette')
                exposureOffsetSlider = gr.Slider(
                    0, 1, 0, step=.05, label='Exposure offset')
                hdrSlider = gr.Slider(0, 1, 0, label='HDR')

                bestChoiceButton = gr.Button(value="Best Choice")
                bestChoiceButton.click(bestChoiceValues, inputs=[saturationSlider, temperatureSlider, brightnessSlider, contrastSlider, sharpnessSlider, blurSlider, noiseSlider, vignetteSlider, exposureOffsetSlider, hdrSlider],
                                       outputs=[saturationSlider, temperatureSlider, brightnessSlider, contrastSlider, sharpnessSlider, blurSlider, noiseSlider, vignetteSlider, exposureOffsetSlider, hdrSlider])

                resetSlidersButton = gr.Button(value="Reset Sliders")
                resetSlidersButton.click(resetValues, inputs=[saturationSlider, temperatureSlider, brightnessSlider, contrastSlider, sharpnessSlider, blurSlider, noiseSlider, vignetteSlider, exposureOffsetSlider, hdrSlider],
                                         outputs=[saturationSlider, temperatureSlider, brightnessSlider, contrastSlider, sharpnessSlider, blurSlider, noiseSlider, vignetteSlider, exposureOffsetSlider, hdrSlider])

            with gr.Tab(label='Effects', id=3):
                lensDistortionRadioButton = gr.Radio(
                    ["None", "Lens Distortion", "Fish Eye"], label="Lens effect", value="None")
                chromaticAberrationSlider = gr.Slider(
                    0, 1, 0, label='Chromatic aberration')

            with gr.Tab(label='Custom EXIF', id=4):
                customEXIF = gr.TextArea(
                    label="Here you can fill in your custom EXIF")

            return [enabled, saturationSlider, temperatureSlider, brightnessSlider, contrastSlider, sharpnessSlider, blurSlider, noiseSlider, vignetteSlider, exposureOffsetSlider, hdrSlider,
                    clearEXIFCheckbox, flipImageCheckbox, dontShowOriginalCheckbox, lensDistortionRadioButton, chromaticAberrationSlider, customEXIF]

    def postprocess(self, p, processed, enabled, saturationSlider, temperatureSlider, brightnessSlider, contrastSlider, sharpnessSlider, blurSlider, noiseSlider, vignetteSlider, exposureOffsetSlider, hdrSlider,
                    clearEXIFCheckbox, flipImageCheckbox, dontShowOriginalCheckbox, lensDistortionRadioButton, chromaticAberrationSlider, customEXIF):

        if not enabled:
            return

        proc = processed
        image = proc.images[0]
        img = ImageEnhance.Color(image).enhance(saturationSlider)
        img = ImageEnhance.Brightness(img).enhance(brightnessSlider)
        img = ImageEnhance.Contrast(img).enhance(contrastSlider)

        if vignetteSlider > 0:
            width, height = img.size
            mask = Image.new("L", (width, height), 0)
            draw = ImageDraw.Draw(mask)
            padding = 100 - vignetteSlider * 100
            draw.ellipse((-padding, -padding, width +
                         padding, height + padding), fill=255)
            mask = mask.filter(ImageFilter.GaussianBlur(radius=100))
            img = Image.composite(img, Image.new(
                "RGB", img.size, "black"), mask)

        if hdrSlider > 0:
            blurred = img.filter(ImageFilter.GaussianBlur(radius=2.8))
            difference = ImageChops.difference(img, blurred)
            sharpEdges = Image.blend(img, difference, 1)

            convertedOriginalImage = np.array(
                image)[:, :, ::-1].copy().astype('float32') / 255.0
            convertedSharped = np.array(
                sharpEdges)[:, :, ::-1].copy().astype('float32') / 255.0

            colorDodge = convertedOriginalImage / (1 - convertedSharped)
            convertedColorDodge = (
                255 * colorDodge).clip(0, 255).astype(np.uint8)

            tempImage = Image.fromarray(cv2.cvtColor(
                convertedColorDodge, cv2.COLOR_BGR2RGB))
            invertedColorDodge = ImageOps.invert(tempImage)
            blackWhiteColorDodge = ImageEnhance.Color(
                invertedColorDodge).enhance(0)
            hue = blendLayers(tempImage, blackWhiteColorDodge, BlendType.HUE)
            hdrImage = blendLayers(hue, tempImage, BlendType.NORMAL, .7)

            img = blendLayers(img, hdrImage, BlendType.NORMAL,
                              hdrSlider * 2).convert("RGB")

        if sharpnessSlider > 0:
            img = ImageEnhance.Sharpness(img).enhance(
                (sharpnessSlider + 1) * 1.5)

        if blurSlider > 0:
            img = img.filter(ImageFilter.BoxBlur(blurSlider * 10))

        if temperatureSlider != 1:
            pixels = img.load()
            for i in range(img.width):
                for j in range(img.height):
                    (r, g, b) = pixels[i, j]
                    if temperatureSlider > 1:
                        r *= 1 + ((temperatureSlider - 1) / 4)
                        b *= 1 - (((temperatureSlider - 1) / 4))
                    else:
                        r *= 1 - (1 - temperatureSlider) / 4
                        b *= 1 + (((1 - temperatureSlider) / 4))
                    pixels[i, j] = (int(r), int(g), int(b))

        if noiseSlider > 0:
            noise = np.random.randint(0, noiseSlider * 100, img.size, np.uint8)
            noise_img = Image.fromarray(noise, 'L').resize(
                img.size).convert(img.mode)
            img = ImageChops.add(img, noise_img)

        if exposureOffsetSlider > 0:
            np_img = np.array(img).astype(float) + exposureOffsetSlider * 75
            np_img = np.clip(np_img, 0, 255).astype(np.uint8)
            img = Image.fromarray(np_img)
            img = ImageEnhance.Brightness(img).enhance(
                brightnessSlider - exposureOffsetSlider / 4)

        if flipImageCheckbox:
            img = Image.fromarray(np.fliplr(np.array(img)))

        if not clearEXIFCheckbox:
            img.info['parameters'] = proc.info

        if len(customEXIF) > 0:
            img.info['parameters'] = customEXIF

        if lensDistortionRadioButton != "None":
            def add_lens_distortion(img, k1, k2):
                img = np.array(img)[:, :, ::-1].copy()
                rows, cols = img.shape[:2]
                map_x, map_y = np.zeros((rows, cols), np.float32), np.zeros(
                    (rows, cols), np.float32)
                for i in range(rows):
                    for j in range(cols):
                        r = np.sqrt((i - rows/2)**2 + (j - cols/2)**2)
                        x = j + (j - cols/2) * (k1 * r**2 + k2 * r**4)
                        y = i + (i - rows/2) * (k1 * r**2 + k2 * r**4)
                        if x >= 0 and x < cols and y >= 0 and y < rows:
                            map_x[i, j] = x
                            map_y[i, j] = y
                return cv2.remap(img, map_x, map_y, cv2.INTER_LINEAR)

            if lensDistortionRadioButton == "Lens Distortion":
                img = add_lens_distortion(img, 1e-12, -1e-12)
            else:
                img = add_lens_distortion(img, 1e-12, 1e-12)
            img = Image.fromarray(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))

        if chromaticAberrationSlider > 0:
            img = add_chromatic(img, chromaticAberrationSlider + .12, True)

        if dontShowOriginalCheckbox:
            proc.images.clear()

        proc.images.insert(0, img)
        return Processed(p, proc.images, p.seed, '')
