# Python meal automated scheduler

## Create an app password for the Google account you want to send the emails from

By following this [guide](https://support.google.com/accounts/answer/185833?hl=en).

Save the app password carefuly since it'll only be shown once!

## Save it as an environment variable onto `~/.bashrc`

By adding a line at the bottom of the file like:

```
export MENU_PY_PWD=the_password_you_just_generated
```

*For MacOS users*: The file you need to modify in macOS is `~/.bash-profile`

*For Windows users*: Follow this [guide](https://www.devdungeon.com/content/set-environment-variables-windows) to do it either using the GUI or cmd.exe

Once done, for Linux and MacOS users `source` the file you modified and it should be good to go.

## Modify `menu.csv` to your liking

Add or remove meals on whichever column you want to fit your needs and likings :)

## Modify lines 21 and 23 with the sender email and the reciever email

Line 21 should contain the email with which you created the app password. Reciever email is the email where you want to recieve your daily menus.

## Modify lines 25 and 26 to change the subject and add a bit more flair to the body (optional)

Once this is done, the script will be ready to run manually, but to run it automatically, for example 5 minutes after midnight, everyday you need to

## Add script to crontab
*For Linux and macOS users*
Run `crontab -e` and add the following line to the bottom of the file:
```
5 0 * * * /path/to/menu_gen.py
```

*For Windows users*
Unfortunately, I have not tested it on Windows, but [this guide](https://docs.active-directory-wp.com/Usage/How_to_add_a_cron_job_on_Windows/Scheduled_tasks_and_cron_jobs_on_Windows/index.html) on Scheduled Tasks seems very well written