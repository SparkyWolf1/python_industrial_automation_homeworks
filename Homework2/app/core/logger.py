import logging.config
import logging
import json
import pathlib
from typing import override
import datetime

logger = logging.getLogger("Main Logger")


class JsonFormatter(logging.Formatter):
    def __init__(self,
                 *,
                 fmt_keys: dict[str, str] | None = None
                 ):
        super().__init__()
        self.fmt_keys = fmt_keys if fmt_keys is not None else {}

    @override
    def format(self, record: logging.LogRecord) -> str:
        message = self._prepare_dict(record)
        return json.dumps(message, default=str)

    def _prepare_dict(self, record: logging.LogRecord) -> dict:
        always_fields = {
            "message": record.getMessage(),
            "timestamp": datetime.datetime.fromtimestamp(
                record.created, tz=datetime.timezone.utc
                ).isoformat(),
        }

        if record.exc_info is not None:
            always_fields["exec_info"] = self.formatException(record.exc_info)

        if record.stack_info is not None:
            always_fields["stack_info"] = self.formatStack(record.stack_info)

        message = {

            key: msg_val
            if (msg_val := always_fields.pop(val, None)) is not None
            else getattr(record, val)
            for key, val in self.fmt_keys.items()
        }
        message.update(always_fields)
        return message


def setup_logging(path: pathlib.Path | None = None) -> None:
    config_file = path / 'logging_config.json'
    if config_file.exists():
        with open(config_file, 'rt') as f:
            config_dict = json.load(f)
        logging.config.dictConfig(config_dict)
        logger.info(f"Logging configured using {config_file.resolve()}")
    else:
        raise FileNotFoundError(
            f"Logging configuration file not found: {config_file.resolve()}")
