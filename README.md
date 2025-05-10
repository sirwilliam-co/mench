````markdown
# 🎲 پروژه‌ی بازی منچ (Mench) - چندنفره با رابط گرافیکی تحت وب

این پروژه نسخه‌ای ساده‌شده از بازی کلاسیک **منچ** است که با زبان Python و فریم‌ورک **Flask** توسعه داده شده و قابلیت اجرا در بسترهای **Docker** و **Kubernetes** را دارد. هدف این پروژه ترکیب توسعه وب، داکرایز کردن برنامه، و استقرار اتوماتیک از طریق CI/CD است.

---

## 🔧 تکنولوژی‌های استفاده‌شده

- Python 3.10+
- Flask
- HTML/CSS (Jinja2 templates)
- JavaScript برای تاس گرافیکی
- Docker
- Kubernetes (Minikube)
- GitHub Actions برای CI/CD

---

## 🕹️ ویژگی‌های کلیدی

- رابط گرافیکی زیبا با طراحی شبیه منچ واقعی
- نمایش تاس گرافیکی (1 تا 6)
- پشتیبانی از چند بازیکن هم‌زمان (تا 4 نفر)
- ذخیره وضعیت بازیکن‌ها با session
- انیمیشن حرکت مهره‌ها
- قابلیت اجرا در مرورگرهای مدرن
- آماده برای استقرار در Docker و Kubernetes

---

## 🚀 اجرای محلی

۱. نصب پیش‌نیازها:

```bash
pip install -r requirements.txt
````

۲. اجرای برنامه:

```bash
python app.py
```

۳. سپس مرورگر را باز کنید و بروید به:

```
http://localhost:5000
```

---

## 🐳 اجرای با Docker

۱. ساخت ایمیج:

```bash
docker build -t 1kasra/mench-app .
```

۲. اجرای کانتینر:

```bash
docker run -p 5000:5000 1kasra/mench-app
```

---

## ☸️ استقرار روی Kubernetes (Minikube)

۱. ساخت ایمیج و Push به Docker Hub:

```bash
docker login
docker build -t 1kasra/mench-app:latest .
docker push 1kasra/mench-app:latest
```

۲. اجرای Minikube و Apply فایل‌های YAML:

```bash
minikube start --driver=docker
kubectl apply -f k8s/deployment.yaml
kubectl apply -f k8s/service.yaml
minikube service mench-service
```

---

## 🔁 CI/CD با GitHub Actions

با هر Push به `master`:

* پروژه به‌صورت خودکار Build شده و به DockerHub (1kasra) Push می‌شود.
* فایل workflow در مسیر زیر قرار دارد:

```
.github/workflows/deploy.yml
```

در آن، اطلاعات Docker Hub با `secrets` زیر تنظیم شده‌اند:

* `DOCKER_USERNAME`
* `DOCKER_PASSWORD`

---

## 📁 ساختار پروژه

```
mench-app/
│
├── app.py
├── Dockerfile
├── requirements.txt
├── templates/
│   └── index.html
├── static/
│   └── dice/
│       └── dice1.png تا dice6.png
├── k8s/
│   ├── deployment.yaml
│   └── service.yaml
└── .github/
    └── workflows/
        └── deploy.yml
```

---

## 📷 پیش‌نمایش رابط کاربری

(در این قسمت می‌تونی یک اسکرین‌شات از بازی اضافه کنی)

---

## 👤 توسعه‌دهنده

* 👨‍💻 [sirwilliam-co](https://github.com/sirwilliam-co)
* 📦 Docker Hub: [1kasra](https://hub.docker.com/u/1kasra)

---

## 📄 مجوز

این پروژه تحت مجوز MIT ارائه می‌شود.

```

---


