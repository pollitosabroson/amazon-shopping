import copy
import logging

from manager.amz_manager import AmzManager

logger = logging.getLogger(__name__)


def resolver_single_order(_, info, where: dict = None):
    """Get single Order
    params:
        where(Dcit): dict with id filter
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


def resolver_orders(_, info, where: dict = {}):
    """Get filters orders
    params:
        where(Dcit): dict with filters params.
    """
    params = copy.deepcopy(where) or {}
    if params.get('q'):
        query_text = AmzManager.convert_params_search(
            params.get('q')
        )
        params.pop('q')
        params.update(query_text)
    try:
        orders = list(AmzManager.filter_values(
            query=params
        ))
        payload = {
            "success": True,
            "orders": orders,
            "total": calculate_total(orders)
        }
    except Exception as error:
        payload = {
            "success": False,
            "errors": [str(error)]
        }
    return payload


def calculate_total(orders):
    """Calculate total orders
    params:
        orders(Collection): Collection with orders
    """
    total = 0
    for order in orders:
        total += order.get('total_owed')
    return total
