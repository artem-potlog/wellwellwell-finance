# Deploying wellwellwell.finance on Render

**Cost:** Free tier available (spins down after 15 min inactivity; $7/mo to keep always on)

---

## Part 1 — Push your code to GitHub

Render deploys from a Git repo.

### 1.1 Create a GitHub repo

1. Go to https://github.com/new
2. Name it `wellwellwell-finance`
3. Set it to **Private**
4. Do NOT add a README (you already have files)

### 1.2 Push your code

Open a terminal in `D:\Fin_Quiz` and run:

```
git init
git add .
git commit -m "Initial commit"
git branch -M main
git remote add origin https://github.com/YOUR_GITHUB_USERNAME/wellwellwell-finance.git
git push -u origin main
```

**Before pushing**, verify `.env` is NOT included:

```
git status
```

Your `.gitignore` already excludes `.env` and PDF files. If you see `.env` listed, stop and fix.

---

## Part 2 — Deploy on Render

### 2.1 Create a Render account

1. Go to https://render.com
2. Sign up with your GitHub account (easiest — gives Render access to your repos)

### 2.2 Create a new Web Service

1. Click **New** → **Web Service**
2. Connect your GitHub repo (`wellwellwell-finance`)
3. Render should auto-detect settings from `render.yaml`. Verify:

| Setting        | Value                              |
|----------------|------------------------------------|
| Name           | `wellwellwell-finance`             |
| Runtime        | Python                             |
| Build command  | `pip install -r requirements.txt`  |
| Start command  | `gunicorn app:app`                 |

4. If fields are empty, enter the values above manually

### 2.3 Set environment variables

On the service creation page (or later in **Environment** tab):

| Key              | Value                    |
|------------------|--------------------------|
| `OPENAI_API_KEY` | your full API key        |
| `OPENAI_MODEL`   | `gpt-5.4-mini`          |

**Never put your API key in code or Git. Only set it in Render's dashboard.**

### 2.4 Deploy

1. Click **Create Web Service**
2. Render installs dependencies and starts gunicorn — watch the logs
3. When you see `Listening on 0.0.0.0:10000`, it's live
4. Visit your URL: `https://wellwellwell-finance.onrender.com`
5. Test that the quiz works

---

## Part 3 — Point your Namecheap domain to Render

### 3.1 Add custom domain in Render

1. In Render dashboard → your service → **Settings** → **Custom Domains**
2. Click **Add Custom Domain**
3. Enter `wellwellwell.finance`
4. Render shows you the DNS records you need (usually a CNAME or A record)
5. Also add `www.wellwellwell.finance` if you want www to work too

### 3.2 Update DNS on Namecheap

1. Log in to https://namecheap.com
2. **Domain List** → **Manage** next to `wellwellwell.finance`
3. Go to the **Advanced DNS** tab
4. Delete any existing A or CNAME records for `@` and `www`
5. Add the records Render told you. Typically:

| Type  | Host | Value                                    | TTL       |
|-------|------|------------------------------------------|-----------|
| A     | @    | the IP address Render shows you          | Automatic |
| CNAME | www  | `wellwellwell-finance.onrender.com`      | Automatic |

6. Save

### 3.3 Wait for DNS + HTTPS

- DNS propagation: **5 min to 48 hours** (usually 15–30 min)
- Check progress: https://dnschecker.org — search for `wellwellwell.finance`
- Once DNS is live, Render auto-provisions a free HTTPS certificate
- Your site will be at: `https://wellwellwell.finance`

---

## Updating the app later

1. Make changes locally in `D:\Fin_Quiz`
2. Push to GitHub:
```
git add .
git commit -m "Description of changes"
git push
```
3. Render auto-detects the push and redeploys (takes ~1 min)

---

## Troubleshooting

**Site shows "Not Found" after DNS change?**
→ DNS is still propagating. Wait and check dnschecker.org.

**App crashes on Render?**
→ Check the **Logs** tab on Render dashboard. Most common: missing environment variable.

**First load is slow (30+ seconds)?**
→ Render free tier spins down after 15 min of inactivity. First visitor wakes it up.
   Upgrade to $7/mo Starter plan to keep it always on.

**Questions fail but site loads?**
→ Check that `OPENAI_API_KEY` is set correctly in Render's Environment tab.

**Want to redeploy without code changes?**
→ Render dashboard → **Manual Deploy** → **Deploy latest commit**.
