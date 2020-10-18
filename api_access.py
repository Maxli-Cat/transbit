import fitbit
import datetime

keys = open("C:\\Keys\\fitbit.txt").read().split()

## You should have a file at that path with ClientID, ClientSecret, access token, and refresh_token
##all on a newline

id, secret, access_token, refresh_token, *_ = keys

authd_client = fitbit.Fitbit(id, secret, access_token=access_token, refresh_token=refresh_token)

sleep = authd_client.sleep()

if __name__ == "__main__":
    print(sleep)