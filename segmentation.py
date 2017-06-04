import cv2
from os.path import join, dirname, realpath

UPLOAD_FOLDER = join(dirname(realpath(__file__)),'templates/traindata/')
UPLOAD_FOLDER2 = join(dirname(realpath(__file__)),'templates/images/')


def segment_digit(file_name, real_image):
    img = cv2.imread(UPLOAD_FOLDER2+file_name)
    img_real = cv2.imread(UPLOAD_FOLDER2+real_image)

    img_final = cv2.imread(file_name)
    img2gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    ret, mask = cv2.threshold(img2gray, 180, 255, cv2.THRESH_BINARY)
    image_final = cv2.bitwise_and(img2gray, img2gray, mask=mask)
    ret, new_img = cv2.threshold(image_final, 180, 255, cv2.THRESH_BINARY)  # for black text , cv.THRESH_BINARY_INV
    '''
            line  8 to 12  : Remove noisy portion 
    '''
    kernel = cv2.getStructuringElement(cv2.MORPH_CROSS, (3,
                                                         3))  # to manipulate the orientation of dilution , large x means horizonatally dilating  more, large y means vertically dilating more
    dilated = cv2.dilate(new_img, kernel, iterations=3)  # dilate , more the iteration more the dilation

    new_para, contours, hierarchy = cv2.findContours(dilated, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)  # get contours

    """
    image, contours, hierarchy = cv2.findContours(dilated,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)  # cv3.x.x 
    """


    index = 0
    our_contours = []


    for contour in contours:
        [x, y, w, h] = cv2.boundingRect(contour)
        our_contours.append([x, y, w, h])

    print(our_contours)
    our_contours.sort()
    print(our_contours)



    rec_file =[]
    for contour in our_contours:
        # get rectangle bounding contour
        [x, y, w, h] = contour

        # Don't plot small false positives that aren't text
        if w < 100 and h < 100:
            continue

        # draw rectangle around contour on original image
        rec = cv2.rectangle(img, (x - 5, y - 5), (x + w + 5, y + h + 5), (255, 0, 255), 2)
        cv2.imwrite(str(UPLOAD_FOLDER2)+"segmented.png", rec)
        # cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 255), 2)


        # you can crop image and send to OCR  , false detected will return no text :)
        cropped = img_real[y - 5:y + h + 5, x - 5: x + w + 5]

        res_cropped = cv2.resize(cropped, (32, 32), interpolation=cv2.INTER_AREA)
        res_cropped_to_eight = cv2.cvtColor(res_cropped, cv2.COLOR_BGR2GRAY)

        s = 'seg' + str(index) + '.png'
        k = 'res' + str(index) + '.png'
        rec_file.append(k);
        print("This is before saving")
        cv2.imwrite(str(UPLOAD_FOLDER2)+s, cropped)
        cv2.imwrite(str(UPLOAD_FOLDER2)+k, res_cropped_to_eight)
        print("This is after saving")
        index = index + 1

    # write original image with added contours to disk
    # cv2.imshow('captcha_result', img)

    return  rec_file







