# qr_dj проект / qr_dj project
#### Проєкт, який створений для генерації ваших qr code! / A project that was created to generate your qr codes!
#### Для вашої зручності буде доступний зручний інтерфейс для реєстрації, авторизації та покупки різноманітних підписок / For your convenience, a convenient interface will be available for registration, authorization and purchase of various subscriptions.

---

## У розробці проекту приймали участь / Participated in the development of the project :
1. [Скрипник Миколай](https://github.com/Nikolay2012) - Керівник проекту / Project manager.
2. [Левковський Дмитро](https://github.com/Levkivskiydmitro) - Тімлід команди / Team leader.
3. [Шматько Дмитро](https://github.com/DimaShmatko999) - Працівник команди / Team worker.
4. [Свистун Артем](https://github.com/asvistun5) - Працівник команди / Team worker.

---

## Використані технології / Technologies used :
### Python 
#### Наша основна мова програмування на якій написан увесь бекенд проекту / Our main programming language in which the entire backend of the project is written.
_нижче приведен фреймворк який було задіяно при написанні сайту_ / _below is the framework that was used when writing the site_
>Django - Головний фреймворк для написання будови сайту / Django - The main framework for writing the site structure.
### HTML
#### Мова-конструктор, на якому побудована структура всіх веб-сторінок проекту / The design language on which the structure of all web pages of the project is built.
### CSS
#### Мова для надання сторінкам стилів і деякого функціоналу / A language for giving pages styles and some functionality.

## Як воно працює? / How it works :
#### Views.py gen_qr
```python
def render_gen_qr(request):
    if request.method == "POST":
        url = request.POST.get("url")
        color = request.POST.get("color")
        bg_color = request.POST.get("bgcolor")
        shape = request.POST.get("shape")
        img = request.POST.get("img")

        if url:
            qr = qrcode.QRCode(
                version=5,
                error_correction=qrcode.constants.ERROR_CORRECT_H,
                box_size=10,
                border=4,
            )
            qr.add_data(url)
            qr.make(fit=True)

            qr_img = qr.make_image(fill=color, back_color="white").convert("RGB")
            qr_size = qr_img.size[0]
    
            styled_qr = Image.new("RGB", (qr_size, qr_size), "white")
            draw = ImageDraw.Draw(styled_qr)

            block_size = qr_size // (qr.modules_count + 2)

            for row in range(qr.modules_count):
                for col in range(qr.modules_count):
                    if qr.modules[row][col]: 
                        x0 = (col + 1) * block_size
                        y0 = (row + 1) * block_size
                        x1 = x0 + block_size
                        y1 = y0 + block_size
                        draw.rounded_rectangle((x0, y0, x1, y1), radius=block_size // 2, fill=color)

            if img:
                try:
                    response = requests.get(img)
                    logo = Image.open(BytesIO(response.content)).convert("RGBA")
                    logo_size = qr_size // 4 
                    logo = logo.resize((logo_size, logo_size))

                    pos = ((qr_size - logo_size) // 2, (qr_size - logo_size) // 2)
                    styled_qr.paste(logo, pos, logo)
                except requests.exceptions.RequestException as e:
                    print(e)

            qr_image_io = BytesIO()
            styled_qr.save(qr_image_io, format="PNG")
            qr_image_io.seek(0)

            qr_code = QR.objects.create(url=url, color=color, shape=shape)
            qr_code.img.save(f"qr_{qr_code.id}.png", ContentFile(qr_image_io.read()))

            return HttpResponseRedirect("home/") 

    return render(request, 'gen.html')
```

#### Views.py reg
```python
def render_reg(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        surname = request.POST.get('surname')
        email = request.POST.get('email')
        password = request.POST.get('password')
        User.objects.create(username= username, surname=surname, email=email, password= password)
        return redirect('auth')
    return render(request, 'reg.html')
```

#### Views.py authorization
```python
def render_auth(request):
    context = {}
    if request.method == 'POST':
        username = request.POST.get('username')
        surname = request.POST.get('surname')
        password = request.POST.get('password')
        user = authenticate(request=request, username=username, surname=surname, password=password, is_auth= True)
        if user:
            login(request=request, user=user)
        else:
            context = {"error": True}
        return redirect('/')
    return render(request, 'auth.html', context=context)
```

#### Models.py gen_qr

```python
class QR(models.Model):
    
    url = models.URLField(max_length=200)
    #size = models.CharField(max_length=10, validators=[validate_size])
    site = models.CharField(max_length=20, default="Youtube")
    color = models.CharField(max_length=20, default="black")
    #bg_color = models.CharField(max_length=20, default="#eceff7")
    shape = models.CharField(max_length=20, default="квадратний")
    img = models.ImageField(upload_to='qr/img')

    date = models.DateField(auto_now=True)


    def __str__(self):
        return f'{self.url}'
```

---

## Для чого було створено цей веб-додаток? / What this web application was created for?
### Для нас створити цей веб-додаток було отримати великий опит! / It was a big survey for us to create this web application!

---

## Висновок: / Conclusion:
### Завдяки цьому проекту ми отримали великий опит, навчилися написанню у фреймворку Django та покращили навички написання HTML та CSS файлів. Також покращили працю з GitHub, и навчилися працювати кожен над своею віткою. / Thanks to this project, we got a lot of experience, learned how to write in the Django framework, and improved our skills in writing HTML and CSS files. We also improved our work with GitHub, and learned how to work on our own branch.
