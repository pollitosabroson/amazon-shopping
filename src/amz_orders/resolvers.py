import copy
import logging

from manager.amz_manager import AmzManager

logger = logging.getLogger(__name__)


def resolve_single_order(_, info, where: dict = None):
    """Get single Order
    params:
        where(Dcit): dict with id fikter
    """
    params = copy.deepcopy(where) or {}
    try:
        payload = {
            "success": True,
            "order": AmzManager.get_by_id(
                value_id=params.get('_id')
            )
        }
    except Exception as error:
        payload = {
            "success": False,
            "errors": [str(error)]
        }
    return payload
