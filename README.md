# Krishi Sahay

KrishiSahay is a project that uses technology to help farmers in India. It focuses on identifying crop diseases quickly and providing solutions that are good for the environment. The project uses a WhatsApp bot because many farmers in India have smartphones and can easily use WhatsApp. The goal is to empower farmers and promote sustainable agriculture.
![alt text](<Screenshot 2024-06-02 at 12.09.09.png>)

## Team Members

[1.Arjun C](H4K3R13)  
[2.Amal K](amalkanhangad)  
[3.Vishnu Prakash J](vishnuprakash-777)  
[4.Hariprasad G Yadhav](HARI-G-YADHAV)

## How it Works ?

[DEMO](https://youtube.com/shorts/Z3PhrI99rhQ?feature=share)

## Technologies used

- flask
- sqlite3
- AI/ML
- Tensorflow

## How to configure

### Prerequisites

#### Create Meta Account

1. A Meta developer account — If you don’t have one, you can [create a Meta developer account here](https://developers.facebook.com/).
2. A business app — If you don't have one, you can [learn to create a business app here](https://developers.facebook.com/docs/development/create-an-app/). If you don't see an option to create a business app, select **Other** > **Next** > **Business**.

#### Create ngrok

1. If you're not an ngrok user yet, just sign up for ngrok for free.
2. Download the ngrok agent.
3. Go to the ngrok dashboard, click Your [Authtoken](https://dashboard.ngrok.com/get-started/your-authtoken), and copy your Authtoken.
4. Follow the instructions to authenticate your ngrok agent. You only have to do this once.
5. On the left menu, expand Cloud Edge and then click Domains.
6. On the Domains page, click + Create Domain or + New Domain. (here everyone can start with [one free domain](https://ngrok.com/blog-post/free-static-domains-ngrok-users))

#### Create `.env`

create a `.env` file inside python-whatsapp-bot directory

```env
ACCESS_TOKEN="<ACCESS_TOKEN>"

APP_ID="<APP_ID>"
APP_SECRET="<APP_SECRET>"
RECIPIENT_WAID="9467XXXXXX" # Your WhatsApp number with country code (e.g., +31612345678)
VERSION="v18.0"
PHONE_NUMBER_ID="<PHONE_NUMBER_ID>"

VERIFY_TOKEN="<VERIFY_TOKEN>"
```

All the values can be found in the meta account

## How to Run

### Run locally

Clone the repository

```bash
https://github.com/H4K3R13/KrishiSahay.git
```

Change the directory

```bash
cd KrishiSahay
```

Setup virtual env

```bash
python3 -m python3 -m venv venv
source venv/bin/activate
```

Install the modules

```bash
pip3 install -r requirements.txt
```

Change directory to bots

```bash
cd python-whatsapp-bot
```

Run flask app

```bash
flask --app run.py --debug run
```

### Run ngrok

Once your app is running successfully on localhost, let's get it on the internet securely using ngrok!

```bash
ngrok http 8000 --domain your-domain.ngrok-free.app
```

8. ngrok will display a URL where your localhost application is exposed to the internet (copy this URL for use with Meta).

### Configure of Webhooks

In the Meta App Dashboard, go to WhatsApp > Configuration, then click the Edit button.

1. In the Edit webhook's callback URL popup, enter the URL provided by the ngrok agent to expose your application to the internet in the Callback URL field, with /webhook at the end (i.e. https://myexample.ngrok-free.app/webhook).
2. Enter a verification token. This string is set up by you when you create your webhook endpoint. You can pick any string you like. Make sure to update this in your `VERIFY_TOKEN` environment variable.

## Other Links

[Presentation](https://drive.google.com/file/d/1jdGcqnBBMfPv0ovjnV8kqJdJP_kDLMHr/view?usp=sharing)
