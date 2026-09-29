import os
from urllib.parse import quote
from flask import Flask, render_template, request, redirect, url_for, flash
app=Flask(__name__)
app.config["SECRET_KEY"]="hotel-management-system-demo"


rooms=[
{"id":1,"name":"Deluxe King Room","type":"Deluxe","price":3500,"description":"A spacious room with a king-size bed, elegant interiors and a relaxing city view.","image":"https://images.unsplash.com/photo-1618773928121-c32242e63f39?auto=format&fit=crop&w=1000&q=85","features":["King Bed","Free Wi-Fi","Breakfast","City View"]},
{"id":2,"name":"Executive Suite","type":"Suite","price":5500,"description":"A premium suite with a separate sitting area, modern bathroom and refined comfort.","image":"https://images.unsplash.com/photo-1582719478250-c89cae4dc85b?auto=format&fit=crop&w=1000&q=85","features":["King Bed","Living Area","Breakfast","Smart TV"]},
{"id":3,"name":"Classic Double Room","type":"Double","price":2500,"description":"A comfortable double room designed for a pleasant stay with all essential facilities.","image":"https://images.unsplash.com/photo-1590490360182-c33d57733427?auto=format&fit=crop&w=1000&q=85","features":["Double Bed","Free Wi-Fi","Breakfast","Air Conditioning"]}
]
gallery_images=[
("Hotel Exterior","https://images.unsplash.com/photo-1566073771259-6a8506099945?auto=format&fit=crop&w=1000&q=85"),
("Luxury Room","https://images.unsplash.com/photo-1611892440504-42a792e24d32?auto=format&fit=crop&w=1000&q=85"),
("Swimming Pool","https://images.unsplash.com/photo-1576013551627-0cc20b96c2a7?auto=format&fit=crop&w=1000&q=85"),
("Restaurant","https://images.unsplash.com/photo-1414235077428-338989a2e8c0?auto=format&fit=crop&w=1000&q=85"),
("Hotel Lobby","https://images.unsplash.com/photo-1564501049412-61c2a3083791?auto=format&fit=crop&w=1000&q=85"),
("Breakfast","https://images.unsplash.com/photo-1533089860892-a7c6f0a88666?auto=format&fit=crop&w=1000&q=85")
]



@app.route("/")
def home(): return render_template("index.html",rooms=rooms,gallery=gallery_images[:4])
@app.route("/about")
def about(): return render_template("about.html")
@app.route("/rooms")
def room_list(): return render_template("rooms.html",rooms=rooms)
@app.route("/gallery")
def gallery(): return render_template("gallery.html",gallery=gallery_images)
@app.route("/contact",methods=["GET","POST"])
def contact():
    if request.method=="POST":
        if not request.form.get("name") or not request.form.get("email") or not request.form.get("message"):
            flash("Please fill in all required fields.","error")
        else:
            flash("Thank you! Your message has been received.","success")
            return redirect(url_for("contact"))
    return render_template("contact.html")
@app.route("/book/<int:room_id>")
def book_room(room_id):
    room=next((r for r in rooms if r["id"]==room_id),None)
    return render_template("booking.html",room=room) if room else ("Room not found",404)
@app.route('/booking-success', methods=['POST'])
def booking_success():
    name = request.form.get('name', '').strip()
    phone = request.form.get('phone', '').strip()
    email = request.form.get('email', '').strip()
    room = request.form.get('room', '').strip()
    check_in = request.form.get('check_in', '').strip()
    check_out = request.form.get('check_out', '').strip()
    guests = request.form.get('guests', '').strip()

    if not name or not phone or not email or not check_in or not check_out:
        flash('Please fill in all required booking fields.', 'error')
        return redirect(request.referrer or url_for('rooms'))

    message = (
        "NEW ROOM BOOKING\n\n"
        f"Guest Name: {name}\n"
        f"Customer Phone: {phone}\n"
        f"Email: {email}\n"
        f"Room: {room}\n"
        f"Check-in: {check_in}\n"
        f"Check-out: {check_out}\n"
        f"Guests: {guests or 'Not specified'}"
    )

    # WhatsApp Click-to-Chat link. This opens WhatsApp with the message pre-filled.
    whatsapp_url = f"https://wa.me/918128353697?text={quote(message)}"
    return redirect(whatsapp_url)

if __name__ == "__main__":
    app.run(debug=True, host="127.0.0.1", port=5000)
