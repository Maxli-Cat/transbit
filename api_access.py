import fitbit

keys = open("C:\\Keys\\fitbit.txt").read().split()
id, secret, access_token, *_ = keys

authd_client = fitbit.Fitbit(id, secret, access_token=access_token)

authd_client.get_sleep()