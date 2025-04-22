"""Class to customize loggers."""

import datetime
import logging
import sys

from dhhdpetlutils.core.enums import Nodenames, LogAuditTrailTopics, LogLevelTags


class CustomLogger:
    """Custom logger class"""

    def __init__(self, logger_filename: str, nodename: Nodenames, logger_name=__name__):
        logging.basicConfig(
            format="%(message)s",
            level=logging.INFO,
            handlers=[
                logging.FileHandler(logger_filename),
                logging.StreamHandler(sys.stdout),
            ],
        )
        self.logger = logging.getLogger(logger_name)
        self.nodename = nodename
        self.dataset = None
        self.input_data_src = None
        self.ehr_id = None
        self.topic = None
        self.openehr_template = None

    def set_dataset(self, dataset: str):
        """
        Set the dataset name.

        Parameters
        ----------
        dataset : str
            Name of the current dataset.
        """
        self.dataset = dataset

    def set_input_data_src(self, input_data_src: str):
        """
        Set the input data source name.

        Parameters
        ----------
        input_data_src : str
            Path to the filename of the current input data source.
        """
        self.input_data_src = input_data_src

    def set_ehr_id(self, ehr_id: str):
        """
        Set the EHR id.

        Parameters
        ----------
        ehr_id : str
            EHR uuid of the current subject.
        """
        self.ehr_id = ehr_id

    def set_topic(self, topic: LogAuditTrailTopics):
        """
        Set the topic.

        Parameters
        ----------
        topic : LogAuditTrailTopics
            Name of the current topic
        """
        self.topic = topic

    def set_openehr_template(self, openehr_template: str):
        """
        Set the openEHR template id.

        Parameters
        ----------
        openehr_template : str
            Name of the current openEHR template id.
        """
        self.openehr_template = openehr_template

    def format_log_message(self, log_level: LogLevelTags, message: str) -> str:
        """
        Format a general log message.


        Parameters
        ----------
        log_level: LogLevelTags
            Log level of the logger
        message : str
            The message describing the event.

        Returns
        -------
        str
            The string of the formatted log message.
        """
        time = datetime.datetime.now()
        millisec = time.strftime(".%f")[:-3]  # convert 6 to 3 millisec digits
        timezone = time.strftime("%z")
        timestamp = time.strftime("%Y-%m-%d %H:%M:%S") + millisec + timezone
        nodename = self.nodename if self.nodename else "N/A"
        dataset = self.dataset if self.dataset else "N/A"
        input_data_src = self.input_data_src if self.input_data_src else "N/A"
        ehr_id = self.ehr_id if self.ehr_id else "N/A"
        topic = self.topic if self.topic else "N/A"
        openehr_template = self.openehr_template if self.openehr_template else "N/A"

        return "[%s][%s][%s][%s][%s][%s][%s][%s] - %s" % (
            timestamp,
            log_level,
            nodename,
            dataset,
            input_data_src,
            ehr_id,
            topic,
            openehr_template,
            message,
        )

    def log_audit_trail_message(self, message: str):
        """
        Log an entry with AUDIT_TRAIL tag and relevant information.

        Parameters
        ----------
        message : str
            The message describing the event.
        """
        self.logger.info(self.format_log_message(LogLevelTags.AUDIT_TRAIL, message))

    def log_warning_message(self, message: str):
        """
        Log an entry with WARNING tag and relevant information.

        Parameters
        ----------
        message : str
            The message describing the event.
        """
        self.logger.warning(self.format_log_message(LogLevelTags.WARNING, message))

    def log_error_message(self, message: str):
        """
        Log an entry with ERROR tag and relevant information.

        Parameters
        ----------
        message : str
            The message describing the event.
        """
        self.logger.error(self.format_log_message(LogLevelTags.ERROR, message))

    def log_info_message(self, message: str):
        """
        Log an entry with INFO tag and relevant information.

        Parameters
        ----------
        message : str
            The message describing the event.
        """
        time = datetime.datetime.now()
        millisec = time.strftime(".%f")[:-3]  # convert 6 to 3 millisec digits
        timezone = time.strftime("%z")
        timestamp = time.strftime("%Y-%m-%d %H:%M:%S") + millisec + timezone
        self.logger.info("[%s][%s][%s] - %s", timestamp, LogLevelTags.INFO, self.nodename, message)
