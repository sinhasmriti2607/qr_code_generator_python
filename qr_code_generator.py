import qrcode
#Taking UPI id as input from user

upi_id = input("Enter your UPI ID:")

#upi://pay?pa=UPI_ID&pn=NAME&am=AMOUNT&cu=CURRENCY&tn=MESSAGE

#Creating Url for different upi apps
phonepay_url = f'upi://pay?pa={upi_id}&pn=Shrishti%20Name&am=10&cu=INR'
paytm_url = f'upi://pay?pa={upi_id}&pn=Shrishti%20Name&am=10&cu=INR'
google_pay_url = f'upi://pay?pa={upi_id}&pn=Shrishti%20Name&am=10&cu=INR'

#Creating QR code or different apps
phonepay_qr = qrcode.make(phonepay_url)
paytm_qr = qrcode.make(paytm_url)
google_pay_qr = qrcode.make(google_pay_url)

#Save qr code to image file
phonepay_qr.save('phonepay_qr.png')
paytm_qr.save('paytm_qr.png')
google_pay_qr.save('google_pay_qr.png')
print("QR codes generated and saved succesfully!")

#Display the qr code(need to install qr code pil/pillow library)
phonepay_qr.show()
paytm_qr.show()
google_pay_qr.show()




