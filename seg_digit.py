import cv2
from os.path import join, dirname, realpath
UPLOAD_FOLDER = join(dirname(realpath(__file__)),'templates/mulsegimages/')

def captch_ex_digits(file_name,img_final,r,d):
    img = cv2.imread(UPLOAD_FOLDER+file_name)

    img_final = cv2.imread(UPLOAD_FOLDER+img_final)
    img2gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    ret, mask = cv2.threshold(img2gray, 180, 255, cv2.THRESH_BINARY)
    image_final = cv2.bitwise_and(img2gray, img2gray, mask=mask)
    ret, new_img = cv2.threshold(image_final, 180, 255, cv2.THRESH_BINARY)  # for black text , cv.THRESH_BINARY_INV
    '''
            line  8 to 12  : Remove noisy portion 
    '''
    kernel = cv2.getStructuringElement(cv2.MORPH_CROSS, (1,
                                                         1))  # to manipulate the orientation of dilution , large x means horizonatally dilating  more, large y means vertically dilating more
    dilated = cv2.dilate(new_img, kernel, iterations=1)  # dilate , more the iteration more the dilation

    # contours, hierarchy = cv2.findContours(dilated, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)  # get contours
    cv2.imwrite(UPLOAD_FOLDER+"final_dialted.png",dilated)



    image, contours, hierarchy = cv2.findContours(dilated,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)  # cv3.x.x

    our_contours = []

    for contour in contours:
        [x, y, w, h] = cv2.boundingRect(contour)
        our_contours.append([x, y, w, h])

    print(our_contours)
    our_contours.sort()
    print(our_contours)

    index = 0
    digits = [];
    # i = 0;
    for contour in our_contours:
        # get rectangle bounding contour
        [x, y, w, h] = contour

        # Don't plot small false positives that aren't text
        if w < 35 and h < 35:
            continue

        # draw rectangle around contour on original image
        rec = cv2.rectangle(img, (x , y ), (x + w , y + h ), (255, 255, 255), 2)
        # cv2.imwrite(UPLOAD_FOLDER + "segmenteddigit"+str(i)+".png", rec)
        # i= i+1


        #you can crop image and send to OCR  , false detected will return no text :)
        cropped = img_final[y :y + h , x : x + w ]

        s = 'digit_' +str(r)+'_'+ str(d)+'_'+str(index) + '.png'
        cv2.imwrite(str(UPLOAD_FOLDER)+s , cropped)
        index = index + 1
        digits.append(s)


    # write original image with added contours to disk
    # cv2.imshow('captcha_result', img)
    # cv2.waitKey()
    return digits


# file_name = 'secondseg0.png'
# img_final = 'secondseg0.png'
# captch_ex_digits(file_name,img_final)