import qrcode
img = qrcode.make('GitHub webhook')
img.save("github_webhook.png")
