"""Utility functions that do not fit elsewhere."""

from .data_structures import LastUpdatedOrderedDict
from .formatting import format_list_nicely, format_number_nicely, format_uav_ids_nicely
from .generic import (
    bind,
    clamp,
    color_to_rgb565,
    color_to_rgb8_triplet,
    consecutive_pairs,
    constant,
    datetime_to_unix_timestamp,
    divide_by,
    identity,
    is_timezone_aware,
    itersubclasses,
    longest_common_prefix,
    multiply_by,
    nop,
    once,
    optional_float,
    optional_int,
    overridden,
    to_uppercase_string,
)
from .system_time import get_current_unix_timestamp_msec

__all__ = (
    "bind",
    "clamp",
    "color_to_rgb565",
    "color_to_rgb8_triplet",
    "consecutive_pairs",
    "constant",
    "datetime_to_unix_timestamp",
    "divide_by",
    "format_list_nicely",
    "format_number_nicely",
    "format_uav_ids_nicely",
    "get_current_unix_timestamp_msec",
    "identity",
    "is_timezone_aware",
    "itersubclasses",
    "LastUpdatedOrderedDict",
    "longest_common_prefix",
    "multiply_by",
    "nop",
    "once",
    "optional_float",
    "optional_int",
    "overridden",
    "to_uppercase_string",
)
