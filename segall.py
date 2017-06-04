import cv2
from os.path import join, dirname, realpath
from conmul import captch_ex_fs
from segment_second import captch_ex_ss
from seg_digit import captch_ex_digits
from trainedNeuralNet import recognize_single
from normalizedata import gray_to_csv



UPLOAD_FOLDER2 = join(dirname(realpath(__file__)),'templates/mulsegimages/')
def identify():
    filename ='median_blurred.png'

    first_segments = captch_ex_fs(filename,filename)
    print(first_segments)

    s=0
    second_segments = []
    for first_segment in first_segments:
        second_segments_each =captch_ex_ss(first_segment,first_segment,s)
        s = s+1
        second_segments.append(second_segments_each)

    print(second_segments)

    r = 0
    digits_all =[]
    for second_segment in second_segments:
        dig_sec =[]
        d = 0
        for digits in second_segment:
            digits_each = captch_ex_digits(digits,digits,r,d)
            d=d+1
            dig_sec.append(digits_each)
        digits_all.append(dig_sec)
        r = r+1;
    print(digits_all)

    r = 0
    digits_all_rec = [];
    for first_segments in digits_all:
        digits_first_rec = []
        for second_segments in first_segments:
            digits_sec_rec =[]
            for digit in second_segments:
                digit_csv = gray_to_csv(digit)
                digit = recognize_single(digit_csv)
                digits_sec_rec.append(digit)
            digits_first_rec.append(digits_sec_rec)
        digits_all_rec.append(digits_first_rec)

    print(digits_all_rec)

    sum_arr = []
    for  first_segment in digits_all_rec:
        for second_segment in first_segment:
            array_size = len(second_segment)-1
            # print(array_size)
            sum = 0
            for digit in second_segment:
                sum = sum + digit*10**array_size
                array_size = array_size-1
            print(sum)
            sum_arr.append(sum)
    return   sum_arr













