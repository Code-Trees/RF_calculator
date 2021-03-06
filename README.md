## This Project can help you calculating Receptive Field in every layer for CNN model ##

# How to use ?  
```python
!pip install rf-calc


from rf_calc import receptive_field
model = models.GoogLeNet().to(device)
image_input_size  = 224
RF = receptive_field(model,image_input_size)
```

# Output 
```python
Kernel_size : Size of the convolving kernel.
Padding : Zero-padding added to both sides of the input image.
Stride : Stride of the convolution. Default: 1
Input_Img_size : Shape of image as input to the layer.
Output_Img_size : Shape of image as Output from the layer.
Receptive_field : Shape pf Receptive field in the layer.

=======================================Reciptive Field Calculator========================================
|    | Kernel_size   | Padding   |   Stride | Input_Img_size   | Output_Img_size   | Receptive_field   |
|---:|:--------------|:----------|---------:|:-----------------|:------------------|:------------------|
|  0 | 7*7           | 3         |        2 | 224*224          | 112*112           | 7*7               |
|  1 | 3*3           | NO        |        2 | 112*112          | 55*55             | 11*11             |
|  2 | 1*1           | NO        |        1 | 55*55            | 55*55             | 11*11             |
|  3 | 3*3           | 1         |        1 | 55*55            | 55*55             | 19*19             |
|  4 | 3*3           | NO        |        2 | 55*55            | 27*27             | 27*27             |
|  5 | 1*1           | NO        |        1 | 27*27            | 27*27             | 27*27             |
|  6 | 1*1           | NO        |        1 | 27*27            | 27*27             | 27*27             |
|  7 | 3*3           | 1         |        1 | 27*27            | 27*27             | 43*43             |
|  8 | 1*1           | NO        |        1 | 27*27            | 27*27             | 43*43             |
|  9 | 3*3           | 1         |        1 | 27*27            | 27*27             | 59*59             |
| 10 | 3*3           | 1         |        1 | 27*27            | 27*27             | 75*75             |
| 11 | 1*1           | NO        |        1 | 27*27            | 27*27             | 75*75             |
| 12 | 1*1           | NO        |        1 | 27*27            | 27*27             | 75*75             |
| 13 | 1*1           | NO        |        1 | 27*27            | 27*27             | 75*75             |
| 14 | 3*3           | 1         |        1 | 27*27            | 27*27             | 91*91             |
| 15 | 1*1           | NO        |        1 | 27*27            | 27*27             | 91*91             |
| 16 | 3*3           | 1         |        1 | 27*27            | 27*27             | 107*107           |
| 17 | 3*3           | 1         |        1 | 27*27            | 27*27             | 123*123           |
| 18 | 1*1           | NO        |        1 | 27*27            | 27*27             | 123*123           |
| 19 | 3*3           | NO        |        2 | 27*27            | 13*13             | 139*139           |
| 20 | 1*1           | NO        |        1 | 13*13            | 13*13             | 139*139           |
| 21 | 1*1           | NO        |        1 | 13*13            | 13*13             | 139*139           |
| 22 | 3*3           | 1         |        1 | 13*13            | 13*13             | 171*171           |
| 23 | 1*1           | NO        |        1 | 13*13            | 13*13             | 171*171           |
| 24 | 3*3           | 1         |        1 | 13*13            | 13*13             | 203*203           |
| 25 | 3*3           | 1         |        1 | 13*13            | 13*13             | 235*235           |
| 26 | 1*1           | NO        |        1 | 13*13            | 13*13             | 235*235           |
| 27 | 1*1           | NO        |        1 | 13*13            | 13*13             | 235*235           |
| 28 | 1*1           | NO        |        1 | 13*13            | 13*13             | 235*235           |
| 29 | 3*3           | 1         |        1 | 13*13            | 13*13             | 267*267           |
| 30 | 1*1           | NO        |        1 | 13*13            | 13*13             | 267*267           |
| 31 | 3*3           | 1         |        1 | 13*13            | 13*13             | 299*299           |
| 32 | 3*3           | 1         |        1 | 13*13            | 13*13             | 331*331           |
| 33 | 1*1           | NO        |        1 | 13*13            | 13*13             | 331*331           |
| 34 | 1*1           | NO        |        1 | 13*13            | 13*13             | 331*331           |
| 35 | 1*1           | NO        |        1 | 13*13            | 13*13             | 331*331           |
| 36 | 3*3           | 1         |        1 | 13*13            | 13*13             | 363*363           |
| 37 | 1*1           | NO        |        1 | 13*13            | 13*13             | 363*363           |
| 38 | 3*3           | 1         |        1 | 13*13            | 13*13             | 395*395           |
| 39 | 3*3           | 1         |        1 | 13*13            | 13*13             | 427*427           |
| 40 | 1*1           | NO        |        1 | 13*13            | 13*13             | 427*427           |
| 41 | 1*1           | NO        |        1 | 13*13            | 13*13             | 427*427           |
| 42 | 1*1           | NO        |        1 | 13*13            | 13*13             | 427*427           |
| 43 | 3*3           | 1         |        1 | 13*13            | 13*13             | 459*459           |
| 44 | 1*1           | NO        |        1 | 13*13            | 13*13             | 459*459           |
| 45 | 3*3           | 1         |        1 | 13*13            | 13*13             | 491*491           |
| 46 | 3*3           | 1         |        1 | 13*13            | 13*13             | 523*523           |
| 47 | 1*1           | NO        |        1 | 13*13            | 13*13             | 523*523           |
| 48 | 1*1           | NO        |        1 | 13*13            | 13*13             | 523*523           |
| 49 | 1*1           | NO        |        1 | 13*13            | 13*13             | 523*523           |
| 50 | 3*3           | 1         |        1 | 13*13            | 13*13             | 555*555           |
| 51 | 1*1           | NO        |        1 | 13*13            | 13*13             | 555*555           |
| 52 | 3*3           | 1         |        1 | 13*13            | 13*13             | 587*587           |
| 53 | 3*3           | 1         |        1 | 13*13            | 13*13             | 619*619           |
| 54 | 1*1           | NO        |        1 | 13*13            | 13*13             | 619*619           |
| 55 | 2*2           | NO        |        2 | 13*13            | 6*6               | 635*635           |
| 56 | 1*1           | NO        |        1 | 6*6              | 6*6               | 635*635           |
| 57 | 1*1           | NO        |        1 | 6*6              | 6*6               | 635*635           |
| 58 | 3*3           | 1         |        1 | 6*6              | 6*6               | 699*699           |
| 59 | 1*1           | NO        |        1 | 6*6              | 6*6               | 699*699           |
| 60 | 3*3           | 1         |        1 | 6*6              | 6*6               | 763*763           |
| 61 | 3*3           | 1         |        1 | 6*6              | 6*6               | 827*827           |
| 62 | 1*1           | NO        |        1 | 6*6              | 6*6               | 827*827           |
| 63 | 1*1           | NO        |        1 | 6*6              | 6*6               | 827*827           |
| 64 | 1*1           | NO        |        1 | 6*6              | 6*6               | 827*827           |
| 65 | 3*3           | 1         |        1 | 6*6              | 6*6               | 891*891           |
| 66 | 1*1           | NO        |        1 | 6*6              | 6*6               | 891*891           |
| 67 | 3*3           | 1         |        1 | 6*6              | 6*6               | 955*955           |
| 68 | 3*3           | 1         |        1 | 6*6              | 6*6               | 1019*1019         |
| 69 | 1*1           | NO        |        1 | 6*6              | 6*6               | 1019*1019         |
| 70 | 1*1           | NO        |        1 | 6*6              | 6*6               | 1019*1019         |
| 71 | 1*1           | NO        |        1 | 6*6              | 6*6               | 1019*1019         |
=========================================================================================================
```

# About Receptive Field

What is Receptive Field ?

1> Local Receptive field
Local receptive field is present in every layer. Local receptive will be the size of kernel used in the layer .For example if we have an image of size 19x19 and we are applying a 3x3 metric then local receptive field will be 3x3 in first layer.

2> Global Receptive field
At every layer the part of image our kernel can see is global receptive field .For a 3x3 kernel convolution global receptive field will increase by 2 units ( there is a mathematical formula that we can cover in later chapters ). It means if you see the below code in every convolution step our model will be able to see 2 pixel more in each side of image .


Input image  =>  kernel shape => Output Image -> local Receptive field -> Global Receptive field 
19x19 => 3x3 => 17x17 -> 3x3 ->3x3
17x17 => 3x3 => 15x15 ->3x3 ->5x5
15x15 => 3x3 => 13x13 ->3x3 ->7x7
13x13 => 3x3 => 11x11 ->3x3 ->9x9
11x11 => 3x3 => 9x9 ->3x3 ->11x11
9x9 => 3x3 => 7x7 ->3x3 ->13x13
7x7 => 3x3 => 5x5 ->3x3 ->15x15
5x5 => 3x3 => 3x3 ->3x3 ->17x17
3x3 => 3x3 => 1x1 ->3x3 ->19x19

Read the article for better understanding.
https://medium.com/@data.pruthiraj/building-blocks-of-computer-vision-and-cnn-f5acdbf3c0b7