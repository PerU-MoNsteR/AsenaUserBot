from pydrive.auth import GoogleAuth


def main():
    gauth = GoogleAuth()
    gauth.LoadCredentialsFile("secret.json")
    if gauth.credentials is None:
        gauth.LocalWebserverAuth()
    elif gauth.access_token_expired:
        gauth.Refresh()
    else:
        gauth.Authorize()
    gauth.SaveCredentialsFile("secret.json")


if __name__ == '__main__':
    main()
