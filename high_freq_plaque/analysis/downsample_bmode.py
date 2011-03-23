#!/usr/bin/env python

import itk
import sys

if len(sys.argv) < 3:
    print('usage: bmodein.mha bmodeout.mha')
    sys.exit(1)

img_type = itk.Image[itk.UC, 3]

reader = itk.ImageFileReader[img_type].New(FileName=sys.argv[1])

filter = itk.ShrinkImageFilter[img_type,img_type].New()
filter.SetInput(reader.GetOutput())
filter.SetShrinkFactor(0,3)
filter.SetShrinkFactor(1,2)

writer = itk.ImageFileWriter[img_type].New(FileName=sys.argv[2])
writer.SetInput(filter.GetOutput())
writer.Update()
