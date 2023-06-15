import cv2

img = cv2.imread("solar-system.jpg")

cv2.putText(img,
            "Sun",
            (30,300),
            cv2.FONT_HERSHEY_COMPLEX,
            1,
            (186,49,11)
)

cv2.putText(img,
            "Mercury",
            (120,250),
            cv2.FONT_HERSHEY_DUPLEX,
            0.5,
            (186,49,11)
)

cv2.putText(img,
            "Venus",
            (190,250),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (186,49,11)
)

cv2.putText(img,
            "Earth",
            (290,270),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (186,49,11)
)

cv2.putText(img,
            "Mars",
            (370,270),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (186,49,11)
)

cv2.putText(img,
            "Jupiter",
            (540,400),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (186,49,11)
)

cv2.putText(img,
            "Saturn",
            (790,300),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (186,49,11)
)

cv2.putText(img,
            "Uranus",
            (990,300),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (186,49,11)
)

cv2.putText(img,
            "Neptune",
            (1090,300),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (186,49,11)
)


cv2.imshow("solar system",img)

cv2.waitKey(0)