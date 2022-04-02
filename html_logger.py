import logging
import datetime
import sys,os


formatter = logging.Formatter('[%(lineno)d]-[%(levelname)s]-[%(threadName)s]-[%(funcName)s]-->%(message)s')
INTRO_LEVEL_NUM=19
CONSOLE_OUT=True


class CustomFormatter(logging.Formatter):
    """Logging Formatter to add colors and count warning / errors"""

    INFO="<p style='margin:10px;padding-top:10px'><span style='border-bottom:2px solid #759B04;text-shadow:1px 1px #09D388;box-shadow:2px 2px 5px;font-family:emoji;font-size:13px;color:#759B04;text-align:right;padding:3px;border-radius:10px;font-style:italic;margin:3px'>  INFO  </span><span style='color:#21AF00;font-style:italic;margin:10px;font-family:emoji;font-size:17px;line-height:1.8'>"
    DEBUG="<p style='margin:10px;padding-top:10px' ><span style='border-bottom:2px solid #0D80F3;border-radius:10px;text-shadow:1px 0px #F20214;box-shadow:2px 2px 5px;font-family:emoji;font-size:11px;color:#0D80F3;text-align:right;padding:2px;border-radius:5px;font-style:italic;margin:3px'>  DEBUG  </span><span style='color:#A104FA;font-style:italic;margin:10px;font-family:emoji;font-size:18px;line-height:1.8'>"
    WARNING="<p style='margin:10px;padding-top:10px' ><span style='border-bottom:2px solid #967311;border-radius:10px;text-shadow:1px 0px #967311;box-shadow:2px 2px 5px;font-family:emoji;font-size:11px;color:#967311;text-align:right;padding:2px;border-radius:5px;font-style:italic;margin:3px'>  WARNING  </span><span style='color:#967311;font-style:italic;margin:10px;font-family:emoji;font-size:18px;line-height:1.8'>"
    ERROR="<p style='margin:10px;padding-top:10px' ><span style='border-bottom:2px solid red;border-radius:10px;text-shadow:1px 0px #F20214;box-shadow:2px 2px 5px;font-family:emoji;font-size:11px;color:#F20214;text-align:right;padding:2px;border-radius:5px;font-style:italic;margin:3px'>  ERROR  </span><span style='color:#F20214;font-style:italic;margin:10px;font-family:emoji;font-size:18px;line-height:1.8'>"
    INTRO="<h2 style='text-align:center;color:#0E4DD1;margin-top:20px;'>"
    END="</span></p>"
    INTRO_END="</h2>"
    format = "%(asctime)s [%(funcName)s] %(message)s"
    INTRO_FORMAT="%(message)s"

    FORMATS = {
        logging.DEBUG: DEBUG + format + END,
        logging.INFO: INFO + format + END,
        logging.WARNING: WARNING + format + END,
        logging.ERROR: ERROR + format + END,
        INTRO_LEVEL_NUM:INTRO+INTRO_FORMAT+INTRO_END
    }

    def format(self, record):
        log_fmt = self.FORMATS.get(record.levelno)
        formatter = logging.Formatter(log_fmt)
        return formatter.format(record)






def intro(self, message, *args, **kws):
    self._log(INTRO_LEVEL_NUM, message, args, **kws)

def base_config(flineame='ses_log',log_path=False):
    path_to_log=BASE_LOGS_PATH if not log_path else log_path
    os.makedirs(path_to_log,exist_ok=True)
    logging.addLevelName(INTRO_LEVEL_NUM, "INTRO")
    logging.Logger.INTRO = intro
    handler = logging.FileHandler(path_to_log + os.sep + f"{flineame}.html", mode='w')
    handler.setFormatter(CustomFormatter())
    logger = logging.getLogger(flineame)
    logger.setLevel(logging.DEBUG)
    logger.addHandler(handler)
    if CONSOLE_OUT:
        logger.addHandler(logging.StreamHandler(sys.stdout))
    logger.info(f"Got Path for log:{flineame} is :{path_to_log}")
    return logger



class htmlTable:
    """
        THIS CLASS IS TO CREATE HTML TABLE. TAKE LIST OF TUPLES AS INPUT
    """
    def __init__(self, head_row_list):
        self.table = """
        <center>
                        <h3>{}</h3>
                        <table cellpadding="4" style="font-family:Georgia;border-collapse: collapse; width:90%;text-align:center;" border="1">
                                    <thead  style="color:white;background-color:#1B2631;font-size:14px">
                                       {}
                                    </thead>
                                <tbody style="color:#34495E">

                                            {}
                                </tbody>
                        </table>

                </center>
                """
        self.header = ''
        self.header_style = " "
        self.row_value = ''
        self.row_final = ''
        self.final_table = ''
        self.loop_count = 0
        self.headrowlist = head_row_list
        self.file_mode = 'w'
        self.table_header = ''
        self.pre_value = ""

    def crete_header(self):
        for row in self.headrowlist:
            self.header = self.header + "<th {}>{}</th>".format(self.header_style, row)

    def create_row(self, rowlist):
        for row in rowlist:
            self.row_value = ''
            for count in range(0, len(row)):
                 self.row_value = self.row_value + "<td>{}</td>".format(str(row[count]))
            self.row_final = self.row_final + "<tr>{}</tr>".format(self.row_value)
        if self.pre_value:
            self.row_final="<tr>{}</tr>".format(self.pre_value)+self.row_final


    def create_custom_row(self,rowdict):
        for key, value in rowdict.items():
            starting_value = "<td rowspan={}>{}</td>".format(len(value) + 1, key)
            row_final = ""
            sorted_dict=self.get_dict(value=value)
            for skey,svalue in sorted_dict.items():
                pre_value = "<td rowspan={}>{}</td>".format(len(svalue), skey)
                for idx,row in  enumerate(svalue):
                    row_value=""
                    for count in range(0, len(row)):
                        row_value = row_value + "<td>{}</td>".format(str(row[count]))
                    if idx>0:
                        row_final = row_final + "<tr>{}</tr>".format(row_value)
                    else:
                        row_final = row_final + "<tr>{}{}</tr>".format(pre_value,row_value)
            self.row_final += "<tr>{}</tr>".format(starting_value) + row_final


    def get_dict(self,value):
        count_dict={}
        for data in value:
                print(data)
                if count_dict.get(data[0]):
                    count_dict[data[0]]= count_dict[data[0]]+[data[1:]]
                else:
                    count_dict[data[0]]=[data[1:]]
        return count_dict



    def create_final_table(self):
        self.final_table = self.table.format(self.table_header, self.header, self.row_final)




