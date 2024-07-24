#    This file is part of the Encoder distribution.
#    Copyright (c) 2021 Danish_00
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, version 3.
#
#    This program is distributed in the hope that it will be useful, but
#    WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
#    General Public License for more details.


import traceback

from decouple import config


class Config:
    def __init__(self):
        try:
            self.ALWAYS_DEPLOY_LATEST = config(
                "ALWAYS_DEPLOY_LATEST", default=False, cast=bool
            )
            self.ALLOW_ACTION = config("ALLOW_ACTION", default=True, cast=bool)
            self.APP_ID = config("APP_ID", default=5929089, cast=int)
            self.API_HASH = config(
                "API_HASH", default="4c188a365d111e459c450333ecfba021"
            )
            self.ARIA2_PORT = config("ARIA2_PORT", default=6800, cast=int)
            self.BOT_TOKEN = config("BOT_TOKEN", default="5606099792:AAHU6Cllh4k6r5x5L0vggl1o5OMlboVZhj0")
            self.CACHE_DL = config("CACHE_DL", default=False, cast=bool)
            self.CAP_DECO = config("CAP_DECO", default="◉")
            self.C_LINK = config("C_LINK", default="Encoded by HyperX")
            self.CMD_SUFFIX = config("CMD_SUFFIX", default=str())
            self.DATABASE_URL = config("DATABASE_URL", default=None)
            self.DBNAME = config("DBNAME", default="ENC")
            self.DEV = config("DEV", default=0, cast=int)
            self.DL_STUFF = config("DL_STUFF", default=None)
            self.DUMP_CHANNEL = config("DUMP_CHANNEL", default=0, cast=int)
            self.DUMP_LEECH = config("DUMP_LEECH", default=True, cast=bool)
            self.DYNO = config("DYNO", default=None)
            self.ENCODER = config("ENCODER", default=None)
            self.EXT_CAP = config("EXTENDED_CAPTIONS", default=True, cast=bool)
            self.FBANNER = config("FBANNER", default=False, cast=bool)
            self.FCHANNEL = config("FCHANNEL", default=0, cast=int)
            self.FCHANNEL_STAT = config("FCHANNEL_STAT", default=0, cast=int)
            self.FCODEC = config("FCODEC", default=None)
            self.FFMPEG = config(
                "FFMPEG",
                default="""ffmpeg -i "{}" -preset veryfast -vf "subtitles='https\:\/\/mindflayersmirror.xuploads.workers.dev\/1\:\/MFmirror\/logo.ass'" -c:v libx265 -s 854x480 -x265-params 'bframes=8:psy-rd=1:ref=3:aq-mode=3:aq-strength=0.8:deblock=1,1' -metadata 'title=Encoded By JAV STORE' -pix_fmt yuv420p -crf 23 -c:a libopus -b:a 128k -map 0 -ac 2 -vbr 2 -level 4.0 -threads 1 "{}"
            """)
            self.FL_CAP = config("FILENAME_AS_CAPTION", default=False, cast=bool)
            self.FS_THRESHOLD = config("FLOOD_SLEEP_THRESHOLD", default=600, cast=int)
            self.FSTICKER = config("FSTICKER", default=None)
            self.LOCK_ON_STARTUP = config("LOCK_ON_STARTUP", default=False, cast=bool)
            self.LOG_CHANNEL = config("LOG_CHANNEL", default=0, cast=int)
            self.LOGS_IN_CHANNEL = config("LOGS_IN_CHANNEL", default=False, cast=bool)
            self.MI_CAP = config("MI_IN_CAPTION", default=True, cast=bool)
            self.MUX_ARGS = config("MUX_ARGS", default=None)
            self.NO_BANNER = config("NO_BANNER", default=False, cast=bool)
            self.NO_TEMP_PM = config("NO_TEMP_PM", default=False, cast=bool)
            self.OVR = config("OVR", default=None)
            self.OWNER = config("OWNER")
            self.PAUSE_ON_DL_INFO = config("PODI", default=True, cast=bool)
            self.QBIT_PORT = config("QBIT_PORT", default=8090, cast=int)
            self.QBIT_TIMEOUT = config("QBIT_TIMEOUT", default=20, cast=int)
            self.RSS_CHAT = config("RSS_CHAT", default=0, cast=int)
            self.RSS_DELAY = config("RSS_DELAY", default=60, cast=int)
            self.RSS_DIRECT = config("RSS_DIRECT", default=False, cast=bool)
            self.RELEASER = config("RELEASER", default="HyperX")
            self.TELEGRAPH_API = config(
                "TELEGRAPH_API", default="https://api.telegra.ph"
            )
            self.TELEGRAPH_AUTHOR = config("TELEGRAPH_AUTHOR", default=None)
            self.TEMP_USER = config("TEMP_USERS", default=str())
            self.TG_DL_CLIENT = config("TG_DL_CLIENT", default="pyrogram")
            self.TG_UL_CLIENT = config("TG_UL_CLIENT", default="pyrogram")
            self.THUMB = config("THUMBNAIL", default="https://telegra.ph/file/cc6cb5448aee307c8f16e.jpg")
            self.FINISHED_PROGRESS_STR = config("FINISHED_PROGRESS_STR", default="🧡")
            self.UN_FINISHED_PROGRESS_STR = config(
                "UN_FINISHED_PROGRESS_STR", default="🤍"
            )
            self.USE_ANILIST = config("USE_ANILIST", default=False, cast=bool)
            self.USE_CAPTION = config("USE_CAPTION", default=False, cast=bool)
            self.WORKERS = config("WORKERS", default=2, cast=int)
        except Exception:
            print("Environment vars Missing; or")
            print("something went wrong")
            print(traceback.format_exc())
            exit()


class Runtime_Config:
    # will slowly replace the Var_list class in utils.bot_utils
    # Progress 1 / 2
    # checking for missed variables
    def __init__(self):
        self.aria2 = None
        self.batch_ing = []
        self.batch_queue = {}
        self.cached = False
        self.cached_dl = False
        self.display_additional_dl_info = False
        self.docker_deployed = False
        self.e_cancel = {}
        self.group_enc = False
        self.groupenc = []
        self.max_message_length = 4096
        self.only_owner_pm = False
        self.pause_status = 0
        self.paused = []
        self.preview_batch = {}
        self.preview_list = []
        self.queue = {}
        self.queue_status = []
        self.r_queue = []
        self.repo_branch = None
        self.rss_dict = {}
        self.rss_ran_once = False
        self.sas = False
        self.sqs = False
        self.started = False
        self.temp_only_in_group = False
        self.temp_users = []
        self.u_cancel = []
        self.version2 = []

conf = Config()
_bot = Runtime_Config()
