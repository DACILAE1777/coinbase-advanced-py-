from typing import Any, Dict, List, Optional

from coinbase.constants import API_PREFIX


def create_order(
    self,
    client_order_id: str,
    product_id: str,
    side: str,
    order_configuration,
    self_trade_prevention_id: Optional[str] = None,
    leverage: Optional[str] = None,
    margin_type: Optional[str] = None,
    retail_portfolio_id: Optional[str] = None,
    **kwargs,
) -> Dict[str, Any]:
    """
    **Create Order**
    ________________

    [POST] https://api.coinbase.com/api/v3/brokerage/orders

    __________

    **Description:**

    Create an order with a specified ``product_id`` (asset-pair), ``side`` (buy/sell), etc.

    __________

    **Read more on the official documentation:** `Create Order
    <https://docs.cdp.coinbase.com/advanced-trade/reference/retailbrokerageapi_postorder>`_
    """
    endpoint = f"{API_PREFIX}/orders"

    data = {
        "client_order_id": client_order_id,
        "product_id": product_id,
        "side": side,
        "order_configuration": order_configuration,
        "self_trade_prevention_id": self_trade_prevention_id,
        "leverage": leverage,
        "margin_type": margin_type,
        "retail_portfolio_id": retail_portfolio_id,
    }

    return self.post(endpoint, data=data, **kwargs)


# Market orders
def market_order(
    self,
    client_order_id: str,
    product_id: str,
    side: str,
    quote_size: Optional[str] = None,
    base_size: Optional[str] = None,
    self_trade_prevention_id: Optional[str] = None,
    leverage: Optional[str] = None,
    margin_type: Optional[str] = None,
    retail_portfolio_id: Optional[str] = None,
    **kwargs,
) -> Dict[str, Any]:
    """
    **Market Order**
    ________________

    [POST] https://api.coinbase.com/api/v3/brokerage/orders

    __________

    **Description:**

    Place a market order to BUY or SELL the desired product at the given market price. If you wish to purchase the
    product, provide a quote_size and if you wish to sell the product, provide a base_size.

    __________

    **Read more on the official documentation:** `Create Order
    <https://docs.cdp.coinbase.com/advanced-trade/reference/retailbrokerageapi_postorder>`_
    """

    market_market_ioc = {"quote_size": quote_size, "base_size": base_size}
    filtered_market_market_ioc = {
        key: value for key, value in market_market_ioc.items() if value is not None
    }

    order_configuration = {"market_market_ioc": filtered_market_market_ioc}

    return create_order(
        self,
        client_order_id,
        product_id,
        side,
        order_configuration,
        self_trade_prevention_id=self_trade_prevention_id,
        leverage=leverage,
        margin_type=margin_type,
        retail_portfolio_id=retail_portfolio_id,
        **kwargs,
    )


def market_order_buy(
    self,
    client_order_id: str,
    product_id: str,
    quote_size: Optional[str] = None,
    base_size: Optional[str] = None,
    self_trade_prevention_id: Optional[str] = None,
    leverage: Optional[str] = None,
    margin_type: Optional[str] = None,
    retail_portfolio_id: Optional[str] = None,
    **kwargs,
) -> Dict[str, Any]:
    """
    **Create Market Order Buy**
    ____________________

    [POST] https://api.coinbase.com/api/v3/brokerage/orders

    __________

    **Description:**

    Place a market order to BUY the desired product at the given market price.

    __________

    **Read more on the official documentation:** `Create Order
    <https://docs.cdp.coinbase.com/advanced-trade/reference/retailbrokerageapi_postorder>`_
    """
    return market_order(
        self,
        client_order_id,
        product_id,
        "BUY",
        quote_size=quote_size,
        base_size=base_size,
        self_trade_prevention_id=self_trade_prevention_id,
        leverage=leverage,
        margin_type=margin_type,
        retail_portfolio_id=retail_portfolio_id,
        **kwargs,
    )


def market_order_sell(
    self,
    client_order_id: str,
    product_id: str,
    base_size: str,
    self_trade_prevention_id: Optional[str] = None,
    leverage: Optional[str] = None,
    margin_type: Optional[str] = None,
    retail_portfolio_id: Optional[str] = None,
    **kwargs,
) -> Dict[str, Any]:
    """
    **Create Market Order Sell**
    _____________________

    [POST] https://api.coinbase.com/api/v3/brokerage/orders

    __________

    **Description:**

    Place a market order to SELL the desired product at the given market price.

    __________

    **Read more on the official documentation:** `Create Order
    <https://docs.cdp.coinbase.com/advanced-trade/reference/retailbrokerageapi_postorder>`_
    """
    return market_order(
        self,
        client_order_id,
        product_id,
        "SELL",
        base_size=base_size,
        self_trade_prevention_id=self_trade_prevention_id,
        leverage=leverage,
        margin_type=margin_type,
        retail_portfolio_id=retail_portfolio_id,
        **kwargs,
    )


# Limit IOC Orders
def limit_order_ioc(
    self,
    client_order_id: str,
    product_id: str,
    side: str,
    base_size: str,
    limit_price: str,
    self_trade_prevention_id: Optional[str] = None,
    leverage: Optional[str] = None,
    margin_type: Optional[str] = None,
    retail_portfolio_id: Optional[str] = None,
    **kwargs,
) -> Dict[str, Any]:
    """
    **Limit IOC Order**
    ________________

    [POST] https://api.coinbase.com/api/v3/brokerage/orders

    __________

    **Description:**

    Place a Limit Order with a IOC time-in-force policy. Provide the base_size (quantity of your base currency to
    spend) as well as a limit_price that indicates the maximum price at which the order should be filled.

    __________

    **Read more on the official documentation:** `Create Order
    <https://docs.cdp.coinbase.com/advanced-trade/reference/retailbrokerageapi_postorder>`_
    """

    sor_limit_ioc = {"base_size": base_size, "limit_price": limit_price}

    order_configuration = {"sor_limit_ioc": sor_limit_ioc}

    return create_order(
        self,
        client_order_id,
        product_id,
        side,
        order_configuration,
        self_trade_prevention_id=self_trade_prevention_id,
        leverage=leverage,
        margin_type=margin_type,
        retail_portfolio_id=retail_portfolio_id,
        **kwargs,
    )


def limit_order_ioc_buy(
    self,
    client_order_id: str,
    product_id: str,
    base_size: str,
    limit_price: str,
    self_trade_prevention_id: Optional[str] = None,
    leverage: Optional[str] = None,
    margin_type: Optional[str] = None,
    retail_portfolio_id: Optional[str] = None,
    **kwargs,
) -> Dict[str, Any]:
    """
    **Limit IOC Order Buy**
    ________________

    [POST] https://api.coinbase.com/api/v3/brokerage/orders

    __________

    **Description:**

    Place a Buy Limit Order with a IOC time-in-force policy. Provide the base_size (quantity of your base currency to
    spend) as well as a limit_price that indicates the maximum price at which the order should be filled.

    __________

    **Read more on the official documentation:** `Create Order
    <https://docs.cdp.coinbase.com/advanced-trade/reference/retailbrokerageapi_postorder>`_
    """

    return limit_order_ioc(
        self,
        client_order_id,
        product_id,
        "BUY",
        base_size=base_size,
        limit_price=limit_price,
        self_trade_prevention_id=self_trade_prevention_id,
        leverage=leverage,
        margin_type=margin_type,
        retail_portfolio_id=retail_portfolio_id,
        **kwargs,
    )


def limit_order_ioc_sell(
    self,
    client_order_id: str,
    product_id: str,
    base_size: str,
    limit_price: str,
    self_trade_prevention_id: Optional[str] = None,
    leverage: Optional[str] = None,
    margin_type: Optional[str] = None,
    retail_portfolio_id: Optional[str] = None,
    **kwargs,
) -> Dict[str, Any]:
    """
    **Limit IOC Order Sell**
    ________________

    [POST] https://api.coinbase.com/api/v3/brokerage/orders

    __________

    **Description:**

    Place a Sell Limit Order with a IOC time-in-force policy. Provide the base_size (quantity of your base currency to
    spend) as well as a limit_price that indicates the maximum price at which the order should be filled.

    __________

    **Read more on the official documentation:** `Create Order
    <https://docs.cdp.coinbase.com/advanced-trade/reference/retailbrokerageapi_postorder>`_
    """

    return limit_order_ioc(
        self,
        client_order_id,
        product_id,
        "SELL",
        base_size=base_size,
        limit_price=limit_price,
        self_trade_prevention_id=self_trade_prevention_id,
        leverage=leverage,
        margin_type=margin_type,
        retail_portfolio_id=retail_portfolio_id,
        **kwargs,
    )


# Limit GTC orders
def limit_order_gtc(
    self,
    client_order_id: str,
    product_id: str,
    side: str,
    base_size: str,
    limit_price: str,
    post_only: bool = False,
    self_trade_prevention_id: Optional[str] = None,
    leverage: Optional[str] = None,
    margin_type: Optional[str] = None,
    retail_portfolio_id: Optional[str] = None,
    **kwargs,
) -> Dict[str, Any]:
    """
    **Limit Order GTC**
    ___________________

    [POST] https://api.coinbase.com/api/v3/brokerage/orders

    __________

    **Description:**

    Place a Limit Order with a GTC time-in-force policy. Provide the base_size (quantity of your base currency to
    spend) as well as a limit_price that indicates the maximum price at which the order should be filled.

    __________

    **Read more on the official documentation:** `Create Order
    <https://docs.cdp.coinbase.com/advanced-trade/reference/retailbrokerageapi_postorder>`_
    """
    order_configuration = {
        "limit_limit_gtc": {
            "base_size": base_size,
            "limit_price": limit_price,
            "post_only": post_only,
        }
    }

    return create_order(
        self,
        client_order_id,
        product_id,
        side,
        order_configuration,
        self_trade_prevention_id=self_trade_prevention_id,
        leverage=leverage,
        margin_type=margin_type,
        retail_portfolio_id=retail_portfolio_id,
        **kwargs,
    )


def limit_order_gtc_buy(
    self,
    client_order_id: str,
    product_id: str,
    base_size: str,
    limit_price: str,
    post_only: bool = False,
    self_trade_prevention_id: Optional[str] = None,
    leverage: Optional[str] = None,
    margin_type: Optional[str] = None,
    retail_portfolio_id: Optional[str] = None,
    **kwargs,
) -> Dict[str, Any]:
    """
    **Limit Order GTC Buy**
    _______________________

    [POST] https://api.coinbase.com/api/v3/brokerage/orders

    __________

    **Description:**

    Place a BUY Limit Order with a GTC time-in-force policy. Provide the base_size (quantity of your base currency to
    spend) as well as a limit_price that indicates the maximum price at which the order should be filled.

    __________

    **Read more on the official documentation:** `Create Order
    <https://docs.cdp.coinbase.com/advanced-trade/reference/retailbrokerageapi_postorder>`_
    """
    return limit_order_gtc(
        self,
        client_order_id,
        product_id,
        "BUY",
        base_size=base_size,
        limit_price=limit_price,
        post_only=post_only,
        self_trade_prevention_id=self_trade_prevention_id,
        leverage=leverage,
        margin_type=margin_type,
        retail_portfolio_id=retail_portfolio_id,
        **kwargs,
    )


def limit_order_gtc_sell(
    self,
    client_order_id: str,
    product_id: str,
    base_size: str,
    limit_price: str,
    post_only: bool = False,
    self_trade_prevention_id: Optional[str] = None,
    leverage: Optional[str] = None,
    margin_type: Optional[str] = None,
    retail_portfolio_id: Optional[str] = None,
    **kwargs,
) -> Dict[str, Any]:
    """
    **Limit Order GTC Sell**
    ________________________

    [POST] https://api.coinbase.com/api/v3/brokerage/orders

    __________

    **Description:**

    Place a SELL Limit Order with a GTC time-in-force policy. Provide the base_size (quantity of your base currency to
    spend) as well as a limit_price that indicates the maximum price at which the order should be filled.

    __________

    **Read more on the official documentation:** `Create Order
    <https://docs.cdp.coinbase.com/advanced-trade/reference/retailbrokerageapi_postorder>`_
    """
    return limit_order_gtc(
        self,
        client_order_id,
        product_id,
        "SELL",
        base_size=base_size,
        limit_price=limit_price,
        post_only=post_only,
        self_trade_prevention_id=self_trade_prevention_id,
        leverage=leverage,
        margin_type=margin_type,
        retail_portfolio_id=retail_portfolio_id,
        **kwargs,
    )


# Limit GTD orders
def limit_order_gtd(
    self,
    client_order_id: str,
    product_id: str,
    side: str,
    base_size: str,
    limit_price: str,
    end_time: str,
    post_only: bool = False,
    self_trade_prevention_id: Optional[str] = None,
    leverage: Optional[str] = None,
    margin_type: Optional[str] = None,
    retail_portfolio_id: Optional[str] = None,
    **kwargs,
) -> Dict[str, Any]:
    """
    **Limit Order GTD**
    ___________________

    [POST] https://api.coinbase.com/api/v3/brokerage/orders

    __________

    **Description:**

    Place a Limit Order with a GTD time-in-force policy. Unlike a Limit Order with a GTC time-in-force policy,
    this order type requires an end-time that indicates when this order should expire.

    __________

    **Read more on the official documentation:** `Create Order
    <https://docs.cdp.coinbase.com/advanced-trade/reference/retailbrokerageapi_postorder>`_
    """
    order_configuration = {
        "limit_limit_gtd": {
            "base_size": base_size,
            "limit_price": limit_price,
            "end_time": end_time,
            "post_only": post_only,
        }
    }

    return create_order(
        self,
        client_order_id,
        product_id,
        side,
        order_configuration,
        self_trade_prevention_id=self_trade_prevention_id,
        leverage=leverage,
        margin_type=margin_type,
        retail_portfolio_id=retail_portfolio_id,
        **kwargs,
    )


def limit_order_gtd_buy(
    self,
    client_order_id: str,
    product_id: str,
    base_size: str,
    limit_price: str,
    end_time: str,
    post_only: bool = False,
    self_trade_prevention_id: Optional[str] = None,
    leverage: Optional[str] = None,
    margin_type: Optional[str] = None,
    retail_portfolio_id: Optional[str] = None,
    **kwargs,
) -> Dict[str, Any]:
    """
    **Limit Order GTD Buy**
    _______________________

    [POST] https://api.coinbase.com/api/v3/brokerage/orders

    __________

    **Description:**

    Place a BUY Limit Order with a GTD time-in-force policy. Unlike a Limit Order with a GTC time-in-force policy,
    this order type requires an end-time that indicates when this order should expire.

    __________

    **Read more on the official documentation:** `Create Order
    <https://docs.cdp.coinbase.com/advanced-trade/reference/retailbrokerageapi_postorder>`_
    """
    return limit_order_gtd(
        self,
        client_order_id,
        product_id,
        "BUY",
        base_size=base_size,
        limit_price=limit_price,
        end_time=end_time,
        post_only=post_only,
        self_trade_prevention_id=self_trade_prevention_id,
        leverage=leverage,
        margin_type=margin_type,
        retail_portfolio_id=retail_portfolio_id,
        **kwargs,
    )


def limit_order_gtd_sell(
    self,
    client_order_id: str,
    product_id: str,
    base_size: str,
    limit_price: str,
    end_time: str,
    post_only: bool = False,
    self_trade_prevention_id: Optional[str] = None,
    leverage: Optional[str] = None,
    margin_type: Optional[str] = None,
    retail_portfolio_id: Optional[str] = None,
    **kwargs,
) -> Dict[str, Any]:
    """
    **Limit Order GTD Sell**
    ________________________

    [POST] https://api.coinbase.com/api/v3/brokerage/orders

    __________

    **Description:**

    Place a SELL Limit Order with a GTD time-in-force policy. Unlike a Limit Order with a GTC time-in-force policy,
    this order type requires an end-time that indicates when this order should expire.

    __________

    **Read more on the official documentation:** `Create Order
    <https://docs.cdp.coinbase.com/advanced-trade/reference/retailbrokerageapi_postorder>`_
    """
    return limit_order_gtd(
        self,
        client_order_id,
        product_id,
        "SELL",
        base_size=base_size,
        limit_price=limit_price,
        end_time=end_time,
        post_only=post_only,
        self_trade_prevention_id=self_trade_prevention_id,
        leverage=leverage,
        margin_type=margin_type,
        retail_portfolio_id=retail_portfolio_id,
        **kwargs,
    )


# Limit FOK Orders
def limit_order_fok(
    self,
    client_order_id: str,
    product_id: str,
    side: str,
    base_size: str,
    limit_price: str,
    self_trade_prevention_id: Optional[str] = None,
    leverage: Optional[str] = None,
    margin_type: Optional[str] = None,
    retail_portfolio_id: Optional[str] = None,
    **kwargs,
) -> Dict[str, Any]:
    """
    **Limit FOK Order**
    ________________

    [POST] https://api.coinbase.com/api/v3/brokerage/orders

    __________

    **Description:**

    Place a Limit Order with a FOK time-in-force policy. Provide the base_size (quantity of your base currency to
    spend) as well as a limit_price that indicates the maximum price at which the order should be filled.

    __________

    **Read more on the official documentation:** `Create Order
    <https://docs.cdp.coinbase.com/advanced-trade/reference/retailbrokerageapi_postorder>`_
    """

    limit_limit_fok = {"base_size": base_size, "limit_price": limit_price}

    order_configuration = {"limit_limit_fok": limit_limit_fok}

    return create_order(
        self,
        client_order_id,
        product_id,
        side,
        order_configuration,
        self_trade_prevention_id=self_trade_prevention_id,
        leverage=leverage,
        margin_type=margin_type,
        retail_portfolio_id=retail_portfolio_id,
        **kwargs,
    )


def limit_order_fok_buy(
    self,
    client_order_id: str,
    product_id: str,
    base_size: str,
    limit_price: str,
    self_trade_prevention_id: Optional[str] = None,
    leverage: Optional[str] = None,
    margin_type: Optional[str] = None,
    retail_portfolio_id: Optional[str] = None,
    **kwargs,
) -> Dict[str, Any]:
    """
    **Limit FOK Order Buy**
    ________________

    [POST] https://api.coinbase.com/api/v3/brokerage/orders

    __________

    **Description:**

    Place a Buy Limit Order with a FOK time-in-force policy. Provide the base_size (quantity of your base currency to
    spend) as well as a limit_price that indicates the maximum price at which the order should be filled.

    __________

    **Read more on the official documentation:** `Create Order
    <https://docs.cdp.coinbase.com/advanced-trade/reference/retailbrokerageapi_postorder>`_
    """

    return limit_order_fok(
        self,
        client_order_id,
        product_id,
        "BUY",
        base_size=base_size,
        limit_price=limit_price,
        self_trade_prevention_id=self_trade_prevention_id,
        leverage=leverage,
        margin_type=margin_type,
        retail_portfolio_id=retail_portfolio_id,
        **kwargs,
    )


def limit_order_fok_sell(
    self,
    client_order_id: str,
    product_id: str,
    base_size: str,
    limit_price: str,
    self_trade_prevention_id: Optional[str] = None,
    leverage: Optional[str] = None,
    margin_type: Optional[str] = None,
    retail_portfolio_id: Optional[str] = None,
    **kwargs,
) -> Dict[str, Any]:
    """
    **Limit FOK Order Sell**
    ________________

    [POST] https://api.coinbase.com/api/v3/brokerage/orders

    __________

    **Description:**

    Place a Sell Limit Order with a FOK time-in-force policy. Provide the base_size (quantity of your base currency to
    spend) as well as a limit_price that indicates the maximum price at which the order should be filled.

    __________

    **Read more on the official documentation:** `Create Order
    <https://docs.cdp.coinbase.com/advanced-trade/reference/retailbrokerageapi_postorder>`_
    """

    return limit_order_fok(
        self,
        client_order_id,
        product_id,
        "SELL",
        base_size=base_size,
        limit_price=limit_price,
        self_trade_prevention_id=self_trade_prevention_id,
        leverage=leverage,
        margin_type=margin_type,
        retail_portfolio_id=retail_portfolio_id,
        **kwargs,
    )


# Stop-Limit GTC orders
def stop_limit_order_gtc(
    self,
    client_order_id: str,
    product_id: str,
    side: str,
    base_size: str,
    limit_price: str,
    stop_price: str,
    stop_direction: str,
    self_trade_prevention_id: Optional[str] = None,
    leverage: Optional[str] = None,
    margin_type: Optional[str] = None,
    retail_portfolio_id: Optional[str] = None,
    **kwargs,
) -> Dict[str, Any]:
    """
    **Stop-Limit Order GTC**
    ________________________

    [POST] https://api.coinbase.com/api/v3/brokerage/orders

    __________

    **Description:**

    Place a Stop Limit order with a GTC time-in-force policy. Stop orders become active and wait to trigger based on
    the movement of the last trade price. The last trade price is the last price at which an order was filled.

    __________

    **Read more on the official documentation:** `Create Order
    <https://docs.cdp.coinbase.com/advanced-trade/reference/retailbrokerageapi_postorder>`_
    """
    order_configuration = {
        "stop_limit_stop_limit_gtc": {
            "base_size": base_size,
            "limit_price": limit_price,
            "stop_price": stop_price,
            "stop_direction": stop_direction,
        }
    }

    return create_order(
        self,
        client_order_id,
        product_id,
        side,
        order_configuration,
        self_trade_prevention_id=self_trade_prevention_id,
        leverage=leverage,
        margin_type=margin_type,
        retail_portfolio_id=retail_portfolio_id,
        **kwargs,
    )


def stop_limit_order_gtc_buy(
    self,
    client_order_id: str,
    product_id: str,
    base_size: str,
    limit_price: str,
    stop_price: str,
    stop_direction: str,
    self_trade_prevention_id: Optional[str] = None,
    leverage: Optional[str] = None,
    margin_type: Optional[str] = None,
    retail_portfolio_id: Optional[str] = None,
    **kwargs,
) -> Dict[str, Any]:
    """
    **Stop-Limit Order GTC Buy**
    ____________________________

    [POST] https://api.coinbase.com/api/v3/brokerage/orders

    __________

    **Description:**

    Place a BUY Stop Limit order with a GTC time-in-force policy. Stop orders become active and wait to trigger based on
    the movement of the last trade price. The last trade price is the last price at which an order was filled.

    __________

    **Read more on the official documentation:** `Create Order
    <https://docs.cdp.coinbase.com/advanced-trade/reference/retailbrokerageapi_postorder>`_
    """
    return stop_limit_order_gtc(
        self,
        client_order_id,
        product_id,
        "BUY",
        base_size=base_size,
        limit_price=limit_price,
        stop_price=stop_price,
        stop_direction=stop_direction,
        self_trade_prevention_id=self_trade_prevention_id,
        leverage=leverage,
        margin_type=margin_type,
        retail_portfolio_id=retail_portfolio_id,
        **kwargs,
    )


def stop_limit_order_gtc_sell(
    self,
    client_order_id: str,
    product_id: str,
    base_size: str,
    limit_price: str,
    stop_price: str,
    stop_direction: str,
    self_trade_prevention_id: Optional[str] = None,
    leverage: Optional[str] = None,
    margin_type: Optional[str] = None,
    retail_portfolio_id: Optional[str] = None,
    **kwargs,
) -> Dict[str, Any]:
    """
    **Stop-Limit Order GTC Sell**
    _____________________________

    [POST] https://api.coinbase.com/api/v3/brokerage/orders

    __________

    **Description:**

    Place a SELL Stop Limit order with a GTC time-in-force policy. Stop orders become active and wait to trigger based on
    the movement of the last trade price. The last trade price is the last price at which an order was filled.

    __________

    **Read more on the official documentation:** `Create Order
    <https://docs.cdp.coinbase.com/advanced-trade/reference/retailbrokerageapi_postorder>`_
    """
    return stop_limit_order_gtc(
        self,
        client_order_id,
        product_id,
        "SELL",
        base_size=base_size,
        limit_price=limit_price,
        stop_price=stop_price,
        stop_direction=stop_direction,
        self_trade_prevention_id=self_trade_prevention_id,
        leverage=leverage,
        margin_type=margin_type,
        retail_portfolio_id=retail_portfolio_id,
        **kwargs,
    )


# Stop-Limit GTD orders
def stop_limit_order_gtd(
    self,
    client_order_id: str,
    product_id: str,
    side: str,
    base_size: str,
    limit_price: str,
    stop_price: str,
    end_time: str,
    stop_direction: str,
    self_trade_prevention_id: Optional[str] = None,
    leverage: Optional[str] = None,
    margin_type: Optional[str] = None,
    retail_portfolio_id: Optional[str] = None,
    **kwargs,
) -> Dict[str, Any]:
    """
    **Stop-Limit Order GTD**
    ________________________

    [POST] https://api.coinbase.com/api/v3/brokerage/orders

    __________

    **Description:**

    Place a Stop Limit order with a GTD time-in-force policy. Stop orders become active and wait to trigger based on
    the movement of the last trade price. The last trade price is the last price at which an order was filled.

    __________

    **Read more on the official documentation:** `Create Order
    <https://docs.cdp.coinbase.com/advanced-trade/reference/retailbrokerageapi_postorder>`_
    """
    order_configuration = {
        "stop_limit_stop_limit_gtd": {
            "base_size": base_size,
            "limit_price": limit_price,
            "stop_price": stop_price,
            "end_time": end_time,
            "stop_direction": stop_direction,
        }
    }

    return create_order(
        self,
        client_order_id,
        product_id,
        side,
        order_configuration,
        self_trade_prevention_id=self_trade_prevention_id,
        leverage=leverage,
        margin_type=margin_type,
        retail_portfolio_id=retail_portfolio_id,
        **kwargs,
    )


def stop_limit_order_gtd_buy(
    self,
    client_order_id: str,
    product_id: str,
    base_size: str,
    limit_price: str,
    stop_price: str,
    end_time: str,
    stop_direction: str,
    self_trade_prevention_id: Optional[str] = None,
    leverage: Optional[str] = None,
    margin_type: Optional[str] = None,
    retail_portfolio_id: Optional[str] = None,
    **kwargs,
) -> Dict[str, Any]:
    """
    **Stop-Limit Order GTD Buy**
    ____________________________

    [POST] https://api.coinbase.com/api/v3/brokerage/orders

    __________

    **Description:**

    Place a BUY Stop Limit order with a GTD time-in-force policy. Stop orders become active and wait to trigger based on
    the movement of the last trade price. The last trade price is the last price at which an order was filled.

    __________

    **Read more on the official documentation:** `Create Order
    <https://docs.cdp.coinbase.com/advanced-trade/reference/retailbrokerageapi_postorder>`_
    """
    return stop_limit_order_gtd(
        self,
        client_order_id,
        product_id,
        "BUY",
        base_size=base_size,
        limit_price=limit_price,
        stop_price=stop_price,
        end_time=end_time,
        stop_direction=stop_direction,
        self_trade_prevention_id=self_trade_prevention_id,
        leverage=leverage,
        margin_type=margin_type,
        retail_portfolio_id=retail_portfolio_id,
        **kwargs,
    )


def stop_limit_order_gtd_sell(
    self,
    client_order_id: str,
    product_id: str,
    base_size: str,
    limit_price: str,
    stop_price: str,
    end_time: str,
    stop_direction: str,
    self_trade_prevention_id: Optional[str] = None,
    leverage: Optional[str] = None,
    margin_type: Optional[str] = None,
    retail_portfolio_id: Optional[str] = None,
    **kwargs,
) -> Dict[str, Any]:
    """
    **Stop-Limit Order GTD Sell**
    _____________________________

    [POST] https://api.coinbase.com/api/v3/brokerage/orders

    __________

    **Description:**

    Place a SELL Stop Limit order with a GTD time-in-force policy. Stop orders become active and wait to trigger based on
    the movement of the last trade price. The last trade price is the last price at which an order was filled.

    __________

    **Read more on the official documentation:** `Create Order
    <https://docs.cdp.coinbase.com/advanced-trade/reference/retailbrokerageapi_postorder>`_
    """
    return stop_limit_order_gtd(
        self,
        client_order_id,
        product_id,
        "SELL",
        base_size=base_size,
        limit_price=limit_price,
        stop_price=stop_price,
        end_time=end_time,
        stop_direction=stop_direction,
        self_trade_prevention_id=self_trade_prevention_id,
        leverage=leverage,
        margin_type=margin_type,
        retail_portfolio_id=retail_portfolio_id,
        **kwargs,
    )


# Trigger Bracket GTC orders
def trigger_bracket_order_gtc(
    self,
    client_order_id: str,
    product_id: str,
    side: str,
    base_size: str,
    limit_price: str,
    stop_trigger_price: str,
    self_trade_prevention_id: Optional[str] = None,
    leverage: Optional[str] = None,
    margin_type: Optional[str] = None,
    retail_portfolio_id: Optional[str] = None,
    **kwargs,
) -> Dict[str, Any]:
    """
    **Trigger Bracket Order GTC**
    ________________________

    [POST] https://api.coinbase.com/api/v3/brokerage/orders

    __________

    **Description:**

    Place a Trigger Bracket order with a GTC time-in-force policy. Trigger Bracket orders become active and wait to trigger based on
    the movement of the last trade price. The last trade price is the last price at which an order was filled.

    __________

    **Read more on the official documentation:** `Create Order
    <https://docs.cdp.coinbase.com/advanced-trade/reference/retailbrokerageapi_postorder>`_
    """
    order_configuration = {
        "trigger_bracket_gtc": {
            "base_size": base_size,
            "limit_price": limit_price,
            "stop_trigger_price": stop_trigger_price,
        }
    }

    return create_order(
        self,
        client_order_id,
        product_id,
        side,
        order_configuration,
        self_trade_prevention_id=self_trade_prevention_id,
        leverage=leverage,
        margin_type=margin_type,
        retail_portfolio_id=retail_portfolio_id,
        **kwargs,
    )


def trigger_bracket_order_gtc_buy(
    self,
    client_order_id: str,
    product_id: str,
    base_size: str,
    limit_price: str,
    stop_trigger_price: str,
    self_trade_prevention_id: Optional[str] = None,
    leverage: Optional[str] = None,
    margin_type: Optional[str] = None,
    retail_portfolio_id: Optional[str] = None,
    **kwargs,
) -> Dict[str, Any]:
    """
    **Trigger Bracket Order GTC Buy**
    ____________________________

    [POST] https://api.coinbase.com/api/v3/brokerage/orders

    __________

    **Description:**

    Place a BUY Trigger Bracket order with a GTC time-in-force policy. Trigger Bracket orders become active and wait to trigger based on
    the movement of the last trade price. The last trade price is the last price at which an order was filled.

    __________

    **Read more on the official documentation:** `Create Order
    <https://docs.cdp.coinbase.com/advanced-trade/reference/retailbrokerageapi_postorder>`_
    """
    return trigger_bracket_order_gtc(
        self,
        client_order_id,
        product_id,
        "BUY",
        base_size=base_size,
        limit_price=limit_price,
        stop_trigger_price=stop_trigger_price,
        self_trade_prevention_id=self_trade_prevention_id,
        leverage=leverage,
        margin_type=margin_type,
        retail_portfolio_id=retail_portfolio_id,
        **kwargs,
    )


def trigger_bracket_order_gtc_sell(
    self,
    client_order_id: str,
    product_id: str,
    base_size: str,
    limit_price: str,
    stop_trigger_price: str,
    self_trade_prevention_id: Optional[str] = None,
    leverage: Optional[str] = None,
    margin_type: Optional[str] = None,
    retail_portfolio_id: Optional[str] = None,
    **kwargs,
) -> Dict[str, Any]:
    """
    **Trigger Bracket Order GTC Sell**
    _____________________________

    [POST] https://api.coinbase.com/api/v3/brokerage/orders

    __________

    **Description:**

    Place a SELL Trigger Bracket order with a GTC time-in-force policy. Trigger Bracket orders become active and wait to trigger based on
    the movement of the last trade price. The last trade price is the last price at which an order was filled.

    __________

    **Read more on the official documentation:** `Create Order
    <https://docs.cdp.coinbase.com/advanced-trade/reference/retailbrokerageapi_postorder>`_
    """
    return trigger_bracket_order_gtc(
        self,
        client_order_id,
        product_id,
        "SELL",
        base_size=base_size,
        limit_price=limit_price,
        stop_trigger_price=stop_trigger_price,
        self_trade_prevention_id=self_trade_prevention_id,
        leverage=leverage,
        margin_type=margin_type,
        retail_portfolio_id=retail_portfolio_id,
        **kwargs,
    )


# Trigger Bracket GTD orders
def trigger_bracket_order_gtd(
    self,
    client_order_id: str,
    product_id: str,
    side: str,
    base_size: str,
    limit_price: str,
    stop_trigger_price: str,
    end_time: str,
    self_trade_prevention_id: Optional[str] = None,
    leverage: Optional[str] = None,
    margin_type: Optional[str] = None,
    retail_portfolio_id: Optional[str] = None,
    **kwargs,
) -> Dict[str, Any]:
    """
    **Trigger Bracket Order GTD**
    ________________________

    [POST] https://api.coinbase.com/api/v3/brokerage/orders

    __________

    **Description:**

    Place a Trigger Bracket order with a GTD time-in-force policy. Trigger Bracket orders become active and wait to trigger based on
    the movement of the last trade price. The last trade price is the last price at which an order was filled.

    __________

    **Read more on the official documentation:** `Create Order
    <https://docs.cdp.coinbase.com/advanced-trade/reference/retailbrokerageapi_postorder>`_
    """
    order_configuration = {
        "trigger_bracket_gtd": {
            "base_size": base_size,
            "limit_price": limit_price,
            "stop_trigger_price": stop_trigger_price,
            "end_time": end_time,
        }
    }

    return create_order(
        self,
        client_order_id,
        product_id,
        side,
        order_configuration,
        self_trade_prevention_id=self_trade_prevention_id,
        leverage=leverage,
        margin_type=margin_type,
        retail_portfolio_id=retail_portfolio_id,
        **kwargs,
    )


def trigger_bracket_order_gtd_buy(
    self,
    client_order_id: str,
    product_id: str,
    base_size: str,
    limit_price: str,
    stop_trigger_price: str,
    end_time: str,
    self_trade_prevention_id: Optional[str] = None,
    leverage: Optional[str] = None,
    margin_type: Optional[str] = None,
    retail_portfolio_id: Optional[str] = None,
    **kwargs,
) -> Dict[str, Any]:
    """
    **Trigger Bracket Order GTD Buy**
    ____________________________

    [POST] https://api.coinbase.com/api/v3/brokerage/orders

    __________

    **Description:**

    Place a BUY Trigger Bracket order with a GTD time-in-force policy. Trigger Bracket orders become active and wait to trigger based on
    the movement of the last trade price. The last trade price is the last price at which an order was filled.

    __________

    **Read more on the official documentation:** `Create Order
    <https://docs.cdp.coinbase.com/advanced-trade/reference/retailbrokerageapi_postorder>`_
    """
    return trigger_bracket_order_gtd(
        self,
        client_order_id,
        product_id,
        "BUY",
        base_size=base_size,
        limit_price=limit_price,
        stop_trigger_price=stop_trigger_price,
        end_time=end_time,
        self_trade_prevention_id=self_trade_prevention_id,
        leverage=leverage,
        margin_type=margin_type,
        retail_portfolio_id=retail_portfolio_id,
        **kwargs,
    )


def trigger_bracket_order_gtd_sell(
    self,
    client_order_id: str,
    product_id: str,
    base_size: str,
    limit_price: str,
    stop_trigger_price: str,
    end_time: str,
    self_trade_prevention_id: Optional[str] = None,
    leverage: Optional[str] = None,
    margin_type: Optional[str] = None,
    retail_portfolio_id: Optional[str] = None,
    **kwargs,
) -> Dict[str, Any]:
    """
    **Trigger Bracket Order GTD Sell**
    _____________________________

    [POST] https://api.coinbase.com/api/v3/brokerage/orders

    __________

    **Description:**

    Place a SELL Trigger Bracket order with a GTD time-in-force policy. Trigger Bracket orders become active and wait to trigger based on
    the movement of the last trade price. The last trade price is the last price at which an order was filled.

    __________

    **Read more on the official documentation:** `Create Order
    <https://docs.cdp.coinbase.com/advanced-trade/reference/retailbrokerageapi_postorder>`_
    """
    return trigger_bracket_order_gtd(
        self,
        client_order_id,
        product_id,
        "SELL",
        base_size=base_size,
        limit_price=limit_price,
        stop_trigger_price=stop_trigger_price,
        end_time=end_time,
        self_trade_prevention_id=self_trade_prevention_id,
        leverage=leverage,
        margin_type=margin_type,
        retail_portfolio_id=retail_portfolio_id,
        **kwargs,
    )


def get_order(self, order_id: str, **kwargs) -> Dict[str, Any]:
    """
    **Get Order**
    _____________

    [GET] https://api.coinbase.com/api/v3/brokerage/orders/historical/{order_id}

    __________

    **Description:**

    Get a single order by order ID.

    __________

    **Read more on the official documentation:** `Get Order
    <https://docs.cdp.coinbase.com/advanced-trade/reference/retailbrokerageapi_gethistoricalorder>`_
    """
    endpoint = f"{API_PREFIX}/orders/historical/{order_id}"

    return self.get(endpoint, **kwargs)


def list_orders(
    self,
    product_id: Optional[str] = None,
    order_status: Optional[List[str]] = None,
    limit: Optional[int] = None,
    start_date: Optional[str] = None,
    end_date: Optional[str] = None,
    order_type: Optional[str] = None,
    order_side: Optional[str] = None,
    cursor: Optional[str] = None,
    product_type: Optional[str] = None,
    order_placement_source: Optional[str] = None,
    contract_expiry_type: Optional[str] = None,
    asset_filters: Optional[List[str]] = None,
    retail_portfolio_id: Optional[str] = None,
    **kwargs,
) -> Dict[str, Any]:
    """
    **List Orders**
    _______________

    [GET] https://api.coinbase.com/api/v3/brokerage/orders/historical/batch

    __________

    **Description:**

    Get a list of orders filtered by optional query parameters (``product_id``, ``order_status``, etc).

    __________

    **Read more on the official documentation:** `List Orders
    <https://docs.cdp.coinbase.com/advanced-trade/reference/retailbrokerageapi_gethistoricalorders>`_
    """
    endpoint = f"{API_PREFIX}/orders/historical/batch"
    params = {
        "product_id": product_id,
        "order_status": order_status,
        "limit": limit,
        "start_date": start_date,
        "end_date": end_date,
        "order_type": order_type,
        "order_side": order_side,
        "cursor": cursor,
        "product_type": product_type,
        "order_placement_source": order_placement_source,
        "contract_expiry_type": contract_expiry_type,
        "asset_filters": asset_filters,
        "retail_portfolio_id": retail_portfolio_id,
    }

    return self.get(endpoint, params=params, **kwargs)


def get_fills(
    self,
    order_id: Optional[str] = None,
    product_id: Optional[str] = None,
    start_sequence_timestamp: Optional[str] = None,
    end_sequence_timestamp: Optional[str] = None,
    limit: Optional[int] = None,
    cursor: Optional[str] = None,
    **kwargs,
) -> Dict[str, Any]:
    """
    **List Fills**
    ______________

    [GET] https://api.coinbase.com/api/v3/brokerage/orders/historical/fills

    __________

    **Description:**

    Get a list of fills filtered by optional query parameters (``product_id``, ``order_id``, etc).

    __________

    **Read more on the official documentation:** `List Fills
    <https://docs.cdp.coinbase.com/advanced-trade/reference/retailbrokerageapi_getfills>`_
    """
    endpoint = f"{API_PREFIX}/orders/historical/fills"
    params = {
        "order_id": order_id,
        "product_id": product_id,
        "start_sequence_timestamp": start_sequence_timestamp,
        "end_sequence_timestamp": end_sequence_timestamp,
        "limit": limit,
        "cursor": cursor,
    }

    return self.get(endpoint, params=params, **kwargs)


def edit_order(
    self,
    order_id: str,
    size: Optional[str] = None,
    price: Optional[str] = None,
    **kwargs,
) -> Dict[str, Any]:
    """
    **Edit Order**
    ______________

    [POST] https://api.coinbase.com/api/v3/brokerage/orders/edit

    __________

    **Description:**

    Edit an order with a specified new ``size``, or new ``price``. Only limit order types, with time in force type of good-till-cancelled can be edited.

    __________

    **Read more on the official documentation:** `Edit Order
    <https://docs.cdp.coinbase.com/advanced-trade/reference/retailbrokerageapi_editorder>`_
    """
    endpoint = f"{API_PREFIX}/orders/edit"
    data = {
        "order_id": order_id,
        "size": size,
        "price": price,
    }

    return self.post(endpoint, data=data, **kwargs)


def preview_edit_order(
    self,
    order_id: str,
    size: Optional[str] = None,
    price: Optional[str] = None,
    **kwargs,
) -> Dict[str, Any]:
    """
    **Preview Edit Order**
    ______________________

    [POST] https://api.coinbase.com/api/v3/brokerage/orders/edit_preview

    __________

    **Description:**

    Simulate an edit order request with a specified new ``size``, or new ``price``, to preview the result of an edit. Only limit order types, with time in force type of good-till-cancelled can be edited.

    __________

    **Read more on the official documentation:** `Edit Order Preview
    <https://docs.cdp.coinbase.com/advanced-trade/reference/retailbrokerageapi_previeweditorder>`_
    """
    endpoint = f"{API_PREFIX}/orders/edit_preview"
    data = {
        "order_id": order_id,
        "size": size,
        "price": price,
    }

    return self.post(endpoint, data=data, **kwargs)


def cancel_orders(self, order_ids: List[str], **kwargs) -> Dict[str, Any]:
    """
    **Cancel Orders**
    _________________

    [POST] https://api.coinbase.com/api/v3/brokerage/orders/batch_cancel

    __________

    **Description:**

    Initiate cancel requests for one or more orders.

    __________

    **Read more on the official documentation:** `Cancel Orders
    <https://docs.cdp.coinbase.com/advanced-trade/reference/retailbrokerageapi_cancelorders>`_
    """
    endpoint = f"{API_PREFIX}/orders/batch_cancel"
    data = {
        "order_ids": order_ids,
    }

    return self.post(endpoint, data=data, **kwargs)


def preview_order(
    self,
    product_id: str,
    side: str,
    order_configuration,
    commission_rate: Optional[str] = None,
    is_max: Optional[bool] = False,
    tradable_balance: Optional[str] = None,
    skip_fcm_risk_check: Optional[bool] = False,
    leverage: Optional[str] = None,
    margin_type: Optional[str] = None,
    retail_portfolio_id: Optional[str] = None,
    **kwargs,
) -> Dict[str, Any]:
    """
    **Preview Order**
    _________________

    [POST] https://api.coinbase.com/api/v3/brokerage/orders/preview

    __________

    **Description:**

    Preview the results of an order request before sending.

    __________

    **Read more on the official documentation:** `Preview Order
    <https://docs.cdp.coinbase.com/advanced-trade/reference/retailbrokerageapi_previeworder>`_
    """
    endpoint = f"{API_PREFIX}/orders/preview"

    if commission_rate:
        commission_rate = {"value": commission_rate}

    data = {
        "product_id": product_id,
        "side": side,
        "order_configuration": order_configuration,
        "commission_rate": commission_rate,
        "is_max": is_max,
        "tradable_balance": tradable_balance,
        "skip_fcm_risk_check": skip_fcm_risk_check,
        "leverage": leverage,
        "margin_type": margin_type,
        "retail_portfolio_id": retail_portfolio_id,
    }

    return self.post(endpoint, data=data, **kwargs)


# Preview market orders
def preview_market_order(
    self,
    product_id: str,
    side: str,
    quote_size: Optional[str] = None,
    base_size: Optional[str] = None,
    commission_rate: Optional[str] = None,
    is_max: Optional[bool] = False,
    tradable_balance: Optional[str] = None,
    skip_fcm_risk_check: Optional[bool] = False,
    leverage: Optional[str] = None,
    margin_type: Optional[str] = None,
    retail_portfolio_id: Optional[str] = None,
    **kwargs,
) -> Dict[str, Any]:
    """
    **Preview Market Order**
    ________________________

    [POST] https://api.coinbase.com/api/v3/brokerage/orders/preview

    __________

    **Description:**

    Preview the results of a market order request before sending.

    __________

    **Read more on the official documentation:** `Preview Order
    <https://docs.cdp.coinbase.com/advanced-trade/reference/retailbrokerageapi_previeworder>`_
    """

    market_market_ioc = {"quote_size": quote_size, "base_size": base_size}
    filtered_market_market_ioc = {
        key: value for key, value in market_market_ioc.items() if value is not None
    }

    order_configuration = {"market_market_ioc": filtered_market_market_ioc}

    return preview_order(
        self,
        product_id,
        side,
        order_configuration,
        commission_rate=commission_rate,
        is_max=is_max,
        tradable_balance=tradable_balance,
        skip_fcm_risk_check=skip_fcm_risk_check,
        leverage=leverage,
        margin_type=margin_type,
        retail_portfolio_id=retail_portfolio_id,
        **kwargs,
    )


def preview_market_order_buy(
    self,
    product_id: str,
    quote_size: Optional[str] = None,
    base_size: Optional[str] = None,
    commission_rate: Optional[str] = None,
    is_max: Optional[bool] = False,
    tradable_balance: Optional[str] = None,
    skip_fcm_risk_check: Optional[bool] = False,
    leverage: Optional[str] = None,
    margin_type: Optional[str] = None,
    retail_portfolio_id: Optional[str] = None,
    **kwargs,
) -> Dict[str, Any]:
    """
    **Preview Market Buy Order**
    ____________________________

    [POST] https://api.coinbase.com/api/v3/brokerage/orders/preview

    __________

    **Description:**

    Preview the results of a market order buy request before sending.

    __________

    **Read more on the official documentation:** `Preview Order
    <https://docs.cdp.coinbase.com/advanced-trade/reference/retailbrokerageapi_previeworder>`_
    """
    return preview_market_order(
        self,
        product_id,
        "BUY",
        quote_size=quote_size,
        base_size=base_size,
        commission_rate=commission_rate,
        is_max=is_max,
        tradable_balance=tradable_balance,
        skip_fcm_risk_check=skip_fcm_risk_check,
        leverage=leverage,
        margin_type=margin_type,
        retail_portfolio_id=retail_portfolio_id,
        **kwargs,
    )


def preview_market_order_sell(
    self,
    product_id: str,
    base_size: str,
    commission_rate: Optional[str] = None,
    is_max: Optional[bool] = False,
    tradable_balance: Optional[str] = None,
    skip_fcm_risk_check: Optional[bool] = False,
    leverage: Optional[str] = None,
    margin_type: Optional[str] = None,
    retail_portfolio_id: Optional[str] = None,
    **kwargs,
) -> Dict[str, Any]:
    """
    **Preview Market Sell Order**
    _____________________________

    [POST] https://api.coinbase.com/api/v3/brokerage/orders/preview

    __________

    **Description:**

    Preview the results of a market order sell request before sending.

    __________

    **Read more on the official documentation:** `Preview Order
    <https://docs.cdp.coinbase.com/advanced-trade/reference/retailbrokerageapi_previeworder>`_
    """
    return preview_market_order(
        self,
        product_id,
        "SELL",
        base_size=base_size,
        commission_rate=commission_rate,
        is_max=is_max,
        tradable_balance=tradable_balance,
        skip_fcm_risk_check=skip_fcm_risk_check,
        leverage=leverage,
        margin_type=margin_type,
        retail_portfolio_id=retail_portfolio_id,
        **kwargs,
    )


# Preview Limit IOC orders
def preview_limit_order_ioc(
    self,
    product_id: str,
    side: str,
    base_size: str,
    limit_price: str,
    commission_rate: Optional[str] = None,
    is_max: Optional[bool] = False,
    tradable_balance: Optional[str] = None,
    skip_fcm_risk_check: Optional[bool] = False,
    leverage: Optional[str] = None,
    margin_type: Optional[str] = None,
    retail_portfolio_id: Optional[str] = None,
    **kwargs,
) -> Dict[str, Any]:
    """
    **Preview Limit Order IOC**
    ___________________________

    [POST] https://api.coinbase.com/api/v3/brokerage/orders/preview

    __________

    **Description:**

    Preview the results of a limit order IOC request before sending.

    __________

    **Read more on the official documentation:** `Preview Order
    <https://docs.cdp.coinbase.com/advanced-trade/reference/retailbrokerageapi_previeworder>`_
    """
    order_configuration = {
        "sor_limit_ioc": {"base_size": base_size, "limit_price": limit_price}
    }

    return preview_order(
        self,
        product_id,
        side,
        order_configuration,
        commission_rate=commission_rate,
        is_max=is_max,
        tradable_balance=tradable_balance,
        skip_fcm_risk_check=skip_fcm_risk_check,
        leverage=leverage,
        margin_type=margin_type,
        retail_portfolio_id=retail_portfolio_id,
        **kwargs,
    )


def preview_limit_order_ioc_buy(
    self,
    product_id: str,
    base_size: str,
    limit_price: str,
    commission_rate: Optional[str] = None,
    is_max: Optional[bool] = False,
    tradable_balance: Optional[str] = None,
    skip_fcm_risk_check: Optional[bool] = False,
    leverage: Optional[str] = None,
    margin_type: Optional[str] = None,
    retail_portfolio_id: Optional[str] = None,
    **kwargs,
) -> Dict[str, Any]:
    """
    **Preview Limit Order IOC Buy**
    ___________________________

    [POST] https://api.coinbase.com/api/v3/brokerage/orders/preview

    __________

    **Description:**

    Preview the results of a limit order IOC buy request before sending.

    __________

    **Read more on the official documentation:** `Preview Order
    <https://docs.cdp.coinbase.com/advanced-trade/reference/retailbrokerageapi_previeworder>`_
    """
    return preview_limit_order_ioc(
        self,
        product_id,
        "BUY",
        base_size=base_size,
        limit_price=limit_price,
        commission_rate=commission_rate,
        is_max=is_max,
        tradable_balance=tradable_balance,
        skip_fcm_risk_check=skip_fcm_risk_check,
        leverage=leverage,
        margin_type=margin_type,
        retail_portfolio_id=retail_portfolio_id,
        **kwargs,
    )


def preview_limit_order_ioc_sell(
    self,
    product_id: str,
    base_size: str,
    limit_price: str,
    commission_rate: Optional[str] = None,
    is_max: Optional[bool] = False,
    tradable_balance: Optional[str] = None,
    skip_fcm_risk_check: Optional[bool] = False,
    leverage: Optional[str] = None,
    margin_type: Optional[str] = None,
    retail_portfolio_id: Optional[str] = None,
    **kwargs,
) -> Dict[str, Any]:
    """
    **Preview Limit Order IOC Sell**
    ___________________________

    [POST] https://api.coinbase.com/api/v3/brokerage/orders/preview

    __________

    **Description:**

    Preview the results of a limit order IOC sell request before sending.

    __________

    **Read more on the official documentation:** `Preview Order
    <https://docs.cdp.coinbase.com/advanced-trade/reference/retailbrokerageapi_previeworder>`_
    """
    return preview_limit_order_ioc(
        self,
        product_id,
        "SELL",
        base_size=base_size,
        limit_price=limit_price,
        commission_rate=commission_rate,
        is_max=is_max,
        tradable_balance=tradable_balance,
        skip_fcm_risk_check=skip_fcm_risk_check,
        leverage=leverage,
        margin_type=margin_type,
        retail_portfolio_id=retail_portfolio_id,
        **kwargs,
    )


# Preview Limit GTC orders
def preview_limit_order_gtc(
    self,
    product_id: str,
    side: str,
    base_size: str,
    limit_price: str,
    post_only: bool = False,
    commission_rate: Optional[str] = None,
    is_max: Optional[bool] = False,
    tradable_balance: Optional[str] = None,
    skip_fcm_risk_check: Optional[bool] = False,
    leverage: Optional[str] = None,
    margin_type: Optional[str] = None,
    retail_portfolio_id: Optional[str] = None,
    **kwargs,
) -> Dict[str, Any]:
    """
    **Preview Limit Order GTC**
    ___________________________

    [POST] https://api.coinbase.com/api/v3/brokerage/orders/preview

    __________

    **Description:**

    Preview the results of a limit order GTC request before sending.

    __________

    **Read more on the official documentation:** `Preview Order
    <https://docs.cdp.coinbase.com/advanced-trade/reference/retailbrokerageapi_previeworder>`_
    """
    order_configuration = {
        "limit_limit_gtc": {
            "base_size": base_size,
            "limit_price": limit_price,
            "post_only": post_only,
        }
    }

    return preview_order(
        self,
        product_id,
        side,
        order_configuration,
        commission_rate=commission_rate,
        is_max=is_max,
        tradable_balance=tradable_balance,
        skip_fcm_risk_check=skip_fcm_risk_check,
        leverage=leverage,
        margin_type=margin_type,
        retail_portfolio_id=retail_portfolio_id,
        **kwargs,
    )


def preview_limit_order_gtc_buy(
    self,
    product_id: str,
    base_size: str,
    limit_price: str,
    post_only: bool = False,
    commission_rate: Optional[str] = None,
    is_max: Optional[bool] = False,
    tradable_balance: Optional[str] = None,
    skip_fcm_risk_check: Optional[bool] = False,
    leverage: Optional[str] = None,
    margin_type: Optional[str] = None,
    retail_portfolio_id: Optional[str] = None,
    **kwargs,
) -> Dict[str, Any]:
    """
    **Preview Limit Order GTC Buy**
    _______________________________

    [POST] https://api.coinbase.com/api/v3/brokerage/orders/preview

    __________

    **Description:**

    Preview the results of a limit order GTC buy request before sending.

    __________

    **Read more on the official documentation:** `Preview Order
    <https://docs.cdp.coinbase.com/advanced-trade/reference/retailbrokerageapi_previeworder>`_
    """
    return preview_limit_order_gtc(
        self,
        product_id,
        "BUY",
        base_size=base_size,
        limit_price=limit_price,
        post_only=post_only,
        commission_rate=commission_rate,
        is_max=is_max,
        tradable_balance=tradable_balance,
        skip_fcm_risk_check=skip_fcm_risk_check,
        leverage=leverage,
        margin_type=margin_type,
        retail_portfolio_id=retail_portfolio_id,
        **kwargs,
    )


def preview_limit_order_gtc_sell(
    self,
    product_id: str,
    base_size: str,
    limit_price: str,
    post_only: bool = False,
    commission_rate: Optional[str] = None,
    is_max: Optional[bool] = False,
    tradable_balance: Optional[str] = None,
    skip_fcm_risk_check: Optional[bool] = False,
    leverage: Optional[str] = None,
    margin_type: Optional[str] = None,
    retail_portfolio_id: Optional[str] = None,
    **kwargs,
) -> Dict[str, Any]:
    """
    **Preview Limit Order GTC Sell**
    ________________________________

    [POST] https://api.coinbase.com/api/v3/brokerage/orders/preview

    __________

    **Description:**

    Preview the results of a limit order GTC sell request before sending.

    __________

    **Read more on the official documentation:** `Preview Order
    <https://docs.cdp.coinbase.com/advanced-trade/reference/retailbrokerageapi_previeworder>`_
    """
    return preview_limit_order_gtc(
        self,
        product_id,
        "SELL",
        base_size=base_size,
        limit_price=limit_price,
        post_only=post_only,
        commission_rate=commission_rate,
        is_max=is_max,
        tradable_balance=tradable_balance,
        skip_fcm_risk_check=skip_fcm_risk_check,
        leverage=leverage,
        margin_type=margin_type,
        retail_portfolio_id=retail_portfolio_id,
        **kwargs,
    )


# Preview Limit GTD orders
def preview_limit_order_gtd(
    self,
    product_id: str,
    side: str,
    base_size: str,
    limit_price: str,
    end_time: str,
    post_only: bool = False,
    commission_rate: Optional[str] = None,
    is_max: Optional[bool] = False,
    tradable_balance: Optional[str] = None,
    skip_fcm_risk_check: Optional[bool] = False,
    leverage: Optional[str] = None,
    margin_type: Optional[str] = None,
    retail_portfolio_id: Optional[str] = None,
    **kwargs,
) -> Dict[str, Any]:
    """
    **Preview Limit Order GTD**
    ___________________________

    [POST] https://api.coinbase.com/api/v3/brokerage/orders/preview

    __________

    **Description:**

    Preview the results of a limit order GTD request before sending.

    __________

    **Read more on the official documentation:** `Preview Order
    <https://docs.cdp.coinbase.com/advanced-trade/reference/retailbrokerageapi_previeworder>`_
    """
    order_configuration = {
        "limit_limit_gtd": {
            "base_size": base_size,
            "limit_price": limit_price,
            "end_time": end_time,
            "post_only": post_only,
        }
    }

    return preview_order(
        self,
        product_id,
        side,
        order_configuration,
        commission_rate=commission_rate,
        is_max=is_max,
        tradable_balance=tradable_balance,
        skip_fcm_risk_check=skip_fcm_risk_check,
        leverage=leverage,
        margin_type=margin_type,
        retail_portfolio_id=retail_portfolio_id,
        **kwargs,
    )


def preview_limit_order_gtd_buy(
    self,
    product_id: str,
    base_size: str,
    limit_price: str,
    end_time: str,
    post_only: bool = False,
    commission_rate: Optional[str] = None,
    is_max: Optional[bool] = False,
    tradable_balance: Optional[str] = None,
    skip_fcm_risk_check: Optional[bool] = False,
    leverage: Optional[str] = None,
    margin_type: Optional[str] = None,
    retail_portfolio_id: Optional[str] = None,
    **kwargs,
) -> Dict[str, Any]:
    """
    **Preview Limit Order GTD Buy**
    _______________________________

    [POST] https://api.coinbase.com/api/v3/brokerage/orders/preview

    __________

    **Description:**

    Preview the results of a limit order GTD buy request before sending.

    __________

    **Read more on the official documentation:** `Preview Order
    <https://docs.cdp.coinbase.com/advanced-trade/reference/retailbrokerageapi_previeworder>`_
    """
    return preview_limit_order_gtd(
        self,
        product_id,
        "BUY",
        base_size=base_size,
        limit_price=limit_price,
        end_time=end_time,
        post_only=post_only,
        commission_rate=commission_rate,
        is_max=is_max,
        tradable_balance=tradable_balance,
        skip_fcm_risk_check=skip_fcm_risk_check,
        leverage=leverage,
        margin_type=margin_type,
        retail_portfolio_id=retail_portfolio_id,
        **kwargs,
    )


def preview_limit_order_gtd_sell(
    self,
    product_id: str,
    base_size: str,
    limit_price: str,
    end_time: str,
    post_only: bool = False,
    commission_rate: Optional[str] = None,
    is_max: Optional[bool] = False,
    tradable_balance: Optional[str] = None,
    skip_fcm_risk_check: Optional[bool] = False,
    leverage: Optional[str] = None,
    margin_type: Optional[str] = None,
    retail_portfolio_id: Optional[str] = None,
    **kwargs,
) -> Dict[str, Any]:
    """
    **Preview Limit Order GTD Sell**
    ________________________________

    [POST] https://api.coinbase.com/api/v3/brokerage/orders/preview

    __________

    **Description:**

    Preview the results of a limit order GTD sell request before sending.

    __________

    **Read more on the official documentation:** `Preview Order
    <https://docs.cdp.coinbase.com/advanced-trade/reference/retailbrokerageapi_previeworder>`_
    """
    return preview_limit_order_gtd(
        self,
        product_id,
        "SELL",
        base_size=base_size,
        limit_price=limit_price,
        end_time=end_time,
        post_only=post_only,
        commission_rate=commission_rate,
        is_max=is_max,
        tradable_balance=tradable_balance,
        skip_fcm_risk_check=skip_fcm_risk_check,
        leverage=leverage,
        margin_type=margin_type,
        retail_portfolio_id=retail_portfolio_id,
        **kwargs,
    )


def preview_limit_order_fok(
    self,
    product_id: str,
    side: str,
    base_size: str,
    limit_price: str,
    commission_rate: Optional[str] = None,
    is_max: Optional[bool] = False,
    tradable_balance: Optional[str] = None,
    skip_fcm_risk_check: Optional[bool] = False,
    leverage: Optional[str] = None,
    margin_type: Optional[str] = None,
    retail_portfolio_id: Optional[str] = None,
    **kwargs,
) -> Dict[str, Any]:
    """
    **Preview Limit Order FOK**
    ___________________________

    [POST] https://api.coinbase.com/api/v3/brokerage/orders/preview

    __________

    **Description:**

    Preview the results of a limit order FOK request before sending.

    __________

    **Read more on the official documentation:** `Preview Order
    <https://docs.cdp.coinbase.com/advanced-trade/reference/retailbrokerageapi_previeworder>`_
    """
    order_configuration = {
        "limit_limit_fok": {"base_size": base_size, "limit_price": limit_price}
    }

    return preview_order(
        self,
        product_id,
        side,
        order_configuration,
        commission_rate=commission_rate,
        is_max=is_max,
        tradable_balance=tradable_balance,
        skip_fcm_risk_check=skip_fcm_risk_check,
        leverage=leverage,
        margin_type=margin_type,
        retail_portfolio_id=retail_portfolio_id,
        **kwargs,
    )


def preview_limit_order_fok_buy(
    self,
    product_id: str,
    base_size: str,
    limit_price: str,
    commission_rate: Optional[str] = None,
    is_max: Optional[bool] = False,
    tradable_balance: Optional[str] = None,
    skip_fcm_risk_check: Optional[bool] = False,
    leverage: Optional[str] = None,
    margin_type: Optional[str] = None,
    retail_portfolio_id: Optional[str] = None,
    **kwargs,
) -> Dict[str, Any]:
    """
    **Preview Limit Order FOK Buy**
    ___________________________

    [POST] https://api.coinbase.com/api/v3/brokerage/orders/preview

    __________

    **Description:**

    Preview the results of a limit order FOK buy request before sending.

    __________

    **Read more on the official documentation:** `Preview Order
    <https://docs.cdp.coinbase.com/advanced-trade/reference/retailbrokerageapi_previeworder>`_
    """
    return preview_limit_order_fok(
        self,
        product_id,
        "BUY",
        base_size=base_size,
        limit_price=limit_price,
        commission_rate=commission_rate,
        is_max=is_max,
        tradable_balance=tradable_balance,
        skip_fcm_risk_check=skip_fcm_risk_check,
        leverage=leverage,
        margin_type=margin_type,
        retail_portfolio_id=retail_portfolio_id,
        **kwargs,
    )


def preview_limit_order_fok_sell(
    self,
    product_id: str,
    base_size: str,
    limit_price: str,
    commission_rate: Optional[str] = None,
    is_max: Optional[bool] = False,
    tradable_balance: Optional[str] = None,
    skip_fcm_risk_check: Optional[bool] = False,
    leverage: Optional[str] = None,
    margin_type: Optional[str] = None,
    retail_portfolio_id: Optional[str] = None,
    **kwargs,
) -> Dict[str, Any]:
    """
    **Preview Limit Order FOK Sell**
    ___________________________

    [POST] https://api.coinbase.com/api/v3/brokerage/orders/preview

    __________

    **Description:**

    Preview the results of a limit order FOK sell request before sending.

    __________

    **Read more on the official documentation:** `Preview Order
    <https://docs.cdp.coinbase.com/advanced-trade/reference/retailbrokerageapi_previeworder>`_
    """
    return preview_limit_order_fok(
        self,
        product_id,
        "SELL",
        base_size=base_size,
        limit_price=limit_price,
        commission_rate=commission_rate,
        is_max=is_max,
        tradable_balance=tradable_balance,
        skip_fcm_risk_check=skip_fcm_risk_check,
        leverage=leverage,
        margin_type=margin_type,
        retail_portfolio_id=retail_portfolio_id,
        **kwargs,
    )


# Preview Stop-Limit GTC orders
def preview_stop_limit_order_gtc(
    self,
    product_id: str,
    side: str,
    base_size: str,
    limit_price: str,
    stop_price: str,
    stop_direction: str,
    commission_rate: Optional[str] = None,
    is_max: Optional[bool] = False,
    tradable_balance: Optional[str] = None,
    skip_fcm_risk_check: Optional[bool] = False,
    leverage: Optional[str] = None,
    margin_type: Optional[str] = None,
    retail_portfolio_id: Optional[str] = None,
    **kwargs,
) -> Dict[str, Any]:
    """
    **Preview Stop-Limit Order GTC**
    ________________________________

    [POST] https://api.coinbase.com/api/v3/brokerage/orders/preview

    __________

    **Description:**

    Preview the results of a stop limit GTC order request before sending.

    __________

    **Read more on the official documentation:** `Preview Order
    <https://docs.cdp.coinbase.com/advanced-trade/reference/retailbrokerageapi_previeworder>`_
    """
    order_configuration = {
        "stop_limit_stop_limit_gtc": {
            "base_size": base_size,
            "limit_price": limit_price,
            "stop_price": stop_price,
            "stop_direction": stop_direction,
        }
    }

    return preview_order(
        self,
        product_id,
        side,
        order_configuration,
        commission_rate=commission_rate,
        is_max=is_max,
        tradable_balance=tradable_balance,
        skip_fcm_risk_check=skip_fcm_risk_check,
        leverage=leverage,
        margin_type=margin_type,
        retail_portfolio_id=retail_portfolio_id,
        **kwargs,
    )


def preview_stop_limit_order_gtc_buy(
    self,
    product_id: str,
    base_size: str,
    limit_price: str,
    stop_price: str,
    stop_direction: str,
    commission_rate: Optional[str] = None,
    is_max: Optional[bool] = False,
    tradable_balance: Optional[str] = None,
    skip_fcm_risk_check: Optional[bool] = False,
    leverage: Optional[str] = None,
    margin_type: Optional[str] = None,
    retail_portfolio_id: Optional[str] = None,
    **kwargs,
) -> Dict[str, Any]:
    """
    **Preview Stop-Limit Order GTC Buy**
    ____________________________________

    [POST] https://api.coinbase.com/api/v3/brokerage/orders/preview

    __________

    **Description:**

    Preview the results of a stop limit GTC order buy request before sending.

    __________

    **Read more on the official documentation:** `Preview Order
    <https://docs.cdp.coinbase.com/advanced-trade/reference/retailbrokerageapi_previeworder>`_
    """
    return preview_stop_limit_order_gtc(
        self,
        product_id,
        "BUY",
        base_size=base_size,
        limit_price=limit_price,
        stop_price=stop_price,
        stop_direction=stop_direction,
        commission_rate=commission_rate,
        is_max=is_max,
        tradable_balance=tradable_balance,
        skip_fcm_risk_check=skip_fcm_risk_check,
        leverage=leverage,
        margin_type=margin_type,
        retail_portfolio_id=retail_portfolio_id,
        **kwargs,
    )


def preview_stop_limit_order_gtc_sell(
    self,
    product_id: str,
    base_size: str,
    limit_price: str,
    stop_price: str,
    stop_direction: str,
    commission_rate: Optional[str] = None,
    is_max: Optional[bool] = False,
    tradable_balance: Optional[str] = None,
    skip_fcm_risk_check: Optional[bool] = False,
    leverage: Optional[str] = None,
    margin_type: Optional[str] = None,
    retail_portfolio_id: Optional[str] = None,
    **kwargs,
) -> Dict[str, Any]:
    """
    **Preview Stop-Limit Order GTC Sell**
    _____________________________________

    [POST] https://api.coinbase.com/api/v3/brokerage/orders/preview

    __________

    **Description:**

    Preview the results of a stop limit GTC order sell request before sending.

    __________

    **Read more on the official documentation:** `Preview Order
    <https://docs.cdp.coinbase.com/advanced-trade/reference/retailbrokerageapi_previeworder>`_
    """
    return preview_stop_limit_order_gtc(
        self,
        product_id,
        "SELL",
        base_size=base_size,
        limit_price=limit_price,
        stop_price=stop_price,
        stop_direction=stop_direction,
        commission_rate=commission_rate,
        is_max=is_max,
        tradable_balance=tradable_balance,
        skip_fcm_risk_check=skip_fcm_risk_check,
        leverage=leverage,
        margin_type=margin_type,
        retail_portfolio_id=retail_portfolio_id,
        **kwargs,
    )


# Preview Stop-Limit GTD orders
def preview_stop_limit_order_gtd(
    self,
    product_id: str,
    side: str,
    base_size: str,
    limit_price: str,
    stop_price: str,
    end_time: str,
    stop_direction: str,
    commission_rate: Optional[str] = None,
    is_max: Optional[bool] = False,
    tradable_balance: Optional[str] = None,
    skip_fcm_risk_check: Optional[bool] = False,
    leverage: Optional[str] = None,
    margin_type: Optional[str] = None,
    retail_portfolio_id: Optional[str] = None,
    **kwargs,
) -> Dict[str, Any]:
    """
    **Preview Stop-Limit Order GTD**
    ________________________________

    [POST] https://api.coinbase.com/api/v3/brokerage/orders/preview

    __________

    **Description:**

    Preview the results of a stop limit GTD order request before sending.

    __________

    **Read more on the official documentation:** `Preview Order
    <https://docs.cdp.coinbase.com/advanced-trade/reference/retailbrokerageapi_previeworder>`_
    """
    order_configuration = {
        "stop_limit_stop_limit_gtd": {
            "base_size": base_size,
            "limit_price": limit_price,
            "stop_price": stop_price,
            "end_time": end_time,
            "stop_direction": stop_direction,
        }
    }

    return preview_order(
        self,
        product_id,
        side,
        order_configuration,
        commission_rate=commission_rate,
        is_max=is_max,
        tradable_balance=tradable_balance,
        skip_fcm_risk_check=skip_fcm_risk_check,
        leverage=leverage,
        margin_type=margin_type,
        retail_portfolio_id=retail_portfolio_id,
        **kwargs,
    )


def preview_stop_limit_order_gtd_buy(
    self,
    product_id: str,
    base_size: str,
    limit_price: str,
    stop_price: str,
    end_time: str,
    stop_direction: str,
    commission_rate: Optional[str] = None,
    is_max: Optional[bool] = False,
    tradable_balance: Optional[str] = None,
    skip_fcm_risk_check: Optional[bool] = False,
    leverage: Optional[str] = None,
    margin_type: Optional[str] = None,
    retail_portfolio_id: Optional[str] = None,
    **kwargs,
) -> Dict[str, Any]:
    """
    **Preview Stop-Limit Order GTD Buy**
    ____________________________________

    [POST] https://api.coinbase.com/api/v3/brokerage/orders/preview

    __________

    **Description:**

    Preview the results of a stop limit GTD order buy request before sending.

    __________

    **Read more on the official documentation:** `Preview Order
    <https://docs.cdp.coinbase.com/advanced-trade/reference/retailbrokerageapi_previeworder>`_
    """
    return preview_stop_limit_order_gtd(
        self,
        product_id,
        "BUY",
        base_size=base_size,
        limit_price=limit_price,
        stop_price=stop_price,
        end_time=end_time,
        stop_direction=stop_direction,
        commission_rate=commission_rate,
        is_max=is_max,
        tradable_balance=tradable_balance,
        skip_fcm_risk_check=skip_fcm_risk_check,
        leverage=leverage,
        margin_type=margin_type,
        retail_portfolio_id=retail_portfolio_id,
        **kwargs,
    )


def preview_stop_limit_order_gtd_sell(
    self,
    product_id: str,
    base_size: str,
    limit_price: str,
    stop_price: str,
    end_time: str,
    stop_direction: str,
    commission_rate: Optional[str] = None,
    is_max: Optional[bool] = False,
    tradable_balance: Optional[str] = None,
    skip_fcm_risk_check: Optional[bool] = False,
    leverage: Optional[str] = None,
    margin_type: Optional[str] = None,
    retail_portfolio_id: Optional[str] = None,
    **kwargs,
) -> Dict[str, Any]:
    """
    **Preview Stop-Limit Order GTD Sell**
    _____________________________________

    [POST] https://api.coinbase.com/api/v3/brokerage/orders/preview

    __________

    **Description:**

    Preview the results of a stop limit GTD order sell request before sending.

    __________

    **Read more on the official documentation:** `Preview Order
    <https://docs.cdp.coinbase.com/advanced-trade/reference/retailbrokerageapi_previeworder>`_
    """
    return preview_stop_limit_order_gtd(
        self,
        product_id,
        "SELL",
        base_size=base_size,
        limit_price=limit_price,
        stop_price=stop_price,
        end_time=end_time,
        stop_direction=stop_direction,
        commission_rate=commission_rate,
        is_max=is_max,
        tradable_balance=tradable_balance,
        skip_fcm_risk_check=skip_fcm_risk_check,
        leverage=leverage,
        margin_type=margin_type,
        retail_portfolio_id=retail_portfolio_id,
        **kwargs,
    )


# Preview Trigger Bracket GTC orders
def preview_trigger_bracket_order_gtc(
    self,
    product_id: str,
    side: str,
    base_size: str,
    limit_price: str,
    stop_trigger_price: str,
    commission_rate: Optional[str] = None,
    is_max: Optional[bool] = False,
    tradable_balance: Optional[str] = None,
    skip_fcm_risk_check: Optional[bool] = False,
    leverage: Optional[str] = None,
    margin_type: Optional[str] = None,
    retail_portfolio_id: Optional[str] = None,
    **kwargs,
) -> Dict[str, Any]:
    """
    **Preview Trigger Bracket Order GTC**
    ________________________________

    [POST] https://api.coinbase.com/api/v3/brokerage/orders/preview

    __________

    **Description:**

    Preview the results of a trigger bracket GTC order request before sending.

    __________

    **Read more on the official documentation:** `Preview Order
    <https://docs.cdp.coinbase.com/advanced-trade/reference/retailbrokerageapi_previeworder>`_
    """
    order_configuration = {
        "trigger_bracket_gtc": {
            "base_size": base_size,
            "limit_price": limit_price,
            "stop_trigger_price": stop_trigger_price,
        }
    }

    return preview_order(
        self,
        product_id,
        side,
        order_configuration,
        commission_rate=commission_rate,
        is_max=is_max,
        tradable_balance=tradable_balance,
        skip_fcm_risk_check=skip_fcm_risk_check,
        leverage=leverage,
        margin_type=margin_type,
        retail_portfolio_id=retail_portfolio_id,
        **kwargs,
    )


def preview_trigger_bracket_order_gtc_buy(
    self,
    product_id: str,
    base_size: str,
    limit_price: str,
    stop_trigger_price: str,
    commission_rate: Optional[str] = None,
    is_max: Optional[bool] = False,
    tradable_balance: Optional[str] = None,
    skip_fcm_risk_check: Optional[bool] = False,
    leverage: Optional[str] = None,
    margin_type: Optional[str] = None,
    retail_portfolio_id: Optional[str] = None,
    **kwargs,
) -> Dict[str, Any]:
    """
    **Preview Trigger Bracket Order GTC Buy**
    ____________________________________

    [POST] https://api.coinbase.com/api/v3/brokerage/orders/preview

    __________

    **Description:**

    Preview the results of a trigger bracket GTC order buy request before sending.

    __________

    **Read more on the official documentation:** `Preview Order
    <https://docs.cdp.coinbase.com/advanced-trade/reference/retailbrokerageapi_previeworder>`_
    """
    return preview_trigger_bracket_order_gtc(
        self,
        product_id,
        "BUY",
        base_size=base_size,
        limit_price=limit_price,
        stop_trigger_price=stop_trigger_price,
        commission_rate=commission_rate,
        is_max=is_max,
        tradable_balance=tradable_balance,
        skip_fcm_risk_check=skip_fcm_risk_check,
        leverage=leverage,
        margin_type=margin_type,
        retail_portfolio_id=retail_portfolio_id,
        **kwargs,
    )


def preview_trigger_bracket_order_gtc_sell(
    self,
    product_id: str,
    base_size: str,
    limit_price: str,
    stop_trigger_price: str,
    commission_rate: Optional[str] = None,
    is_max: Optional[bool] = False,
    tradable_balance: Optional[str] = None,
    skip_fcm_risk_check: Optional[bool] = False,
    leverage: Optional[str] = None,
    margin_type: Optional[str] = None,
    retail_portfolio_id: Optional[str] = None,
    **kwargs,
) -> Dict[str, Any]:
    """
    **Preview Trigger Bracket Order GTC Sell**
    _____________________________________

    [POST] https://api.coinbase.com/api/v3/brokerage/orders/preview

    __________

    **Description:**

    Preview the results of a trigger bracket GTC order sell request before sending.

    __________

    **Read more on the official documentation:** `Preview Order
    <https://docs.cdp.coinbase.com/advanced-trade/reference/retailbrokerageapi_previeworder>`_
    """
    return preview_trigger_bracket_order_gtc(
        self,
        product_id,
        "SELL",
        base_size=base_size,
        limit_price=limit_price,
        stop_trigger_price=stop_trigger_price,
        commission_rate=commission_rate,
        is_max=is_max,
        tradable_balance=tradable_balance,
        skip_fcm_risk_check=skip_fcm_risk_check,
        leverage=leverage,
        margin_type=margin_type,
        retail_portfolio_id=retail_portfolio_id,
        **kwargs,
    )


# Preview Trigger Bracket GTD orders
def preview_trigger_bracket_order_gtd(
    self,
    product_id: str,
    side: str,
    base_size: str,
    limit_price: str,
    stop_trigger_price: str,
    end_time: str,
    commission_rate: Optional[str] = None,
    is_max: Optional[bool] = False,
    tradable_balance: Optional[str] = None,
    skip_fcm_risk_check: Optional[bool] = False,
    leverage: Optional[str] = None,
    margin_type: Optional[str] = None,
    retail_portfolio_id: Optional[str] = None,
    **kwargs,
) -> Dict[str, Any]:
    """
    **Preview Trigger Bracket Order GTD**
    ________________________________

    [POST] https://api.coinbase.com/api/v3/brokerage/orders/preview

    __________

    **Description:**

    Preview the results of a trigger bracket GTD order request before sending.

    __________

    **Read more on the official documentation:** `Preview Order
    <https://docs.cdp.coinbase.com/advanced-trade/reference/retailbrokerageapi_previeworder>`_
    """
    order_configuration = {
        "trigger_bracket_gtd": {
            "base_size": base_size,
            "limit_price": limit_price,
            "stop_trigger_price": stop_trigger_price,
            "end_time": end_time,
        }
    }

    return preview_order(
        self,
        product_id,
        side,
        order_configuration,
        commission_rate=commission_rate,
        is_max=is_max,
        tradable_balance=tradable_balance,
        skip_fcm_risk_check=skip_fcm_risk_check,
        leverage=leverage,
        margin_type=margin_type,
        retail_portfolio_id=retail_portfolio_id,
        **kwargs,
    )


def preview_trigger_bracket_order_gtd_buy(
    self,
    product_id: str,
    base_size: str,
    limit_price: str,
    stop_trigger_price: str,
    end_time: str,
    commission_rate: Optional[str] = None,
    is_max: Optional[bool] = False,
    tradable_balance: Optional[str] = None,
    skip_fcm_risk_check: Optional[bool] = False,
    leverage: Optional[str] = None,
    margin_type: Optional[str] = None,
    retail_portfolio_id: Optional[str] = None,
    **kwargs,
) -> Dict[str, Any]:
    """
    **Preview Trigger Bracket Order GTD Buy**
    ____________________________________

    [POST] https://api.coinbase.com/api/v3/brokerage/orders/preview

    __________

    **Description:**

    Preview the results of a trigger bracket GTD order buy request before sending.

    __________

    **Read more on the official documentation:** `Preview Order
    <https://docs.cdp.coinbase.com/advanced-trade/reference/retailbrokerageapi_previeworder>`_
    """
    return preview_trigger_bracket_order_gtd(
        self,
        product_id,
        "BUY",
        base_size=base_size,
        limit_price=limit_price,
        stop_trigger_price=stop_trigger_price,
        end_time=end_time,
        commission_rate=commission_rate,
        is_max=is_max,
        tradable_balance=tradable_balance,
        skip_fcm_risk_check=skip_fcm_risk_check,
        leverage=leverage,
        margin_type=margin_type,
        retail_portfolio_id=retail_portfolio_id,
        **kwargs,
    )


def preview_trigger_bracket_order_gtd_sell(
    self,
    product_id: str,
    base_size: str,
    limit_price: str,
    stop_trigger_price: str,
    end_time: str,
    commission_rate: Optional[str] = None,
    is_max: Optional[bool] = False,
    tradable_balance: Optional[str] = None,
    skip_fcm_risk_check: Optional[bool] = False,
    leverage: Optional[str] = None,
    margin_type: Optional[str] = None,
    retail_portfolio_id: Optional[str] = None,
    **kwargs,
) -> Dict[str, Any]:
    """
    **Preview Trigger Bracket Order GTD Sell**
    _____________________________________

    [POST] https://api.coinbase.com/api/v3/brokerage/orders/preview

    __________

    **Description:**

    Preview the results of a trigger bracket GTD order sell request before sending.

    __________

    **Read more on the official documentation:** `Preview Order
    <https://docs.cdp.coinbase.com/advanced-trade/reference/retailbrokerageapi_previeworder>`_
    """
    return preview_trigger_bracket_order_gtd(
        self,
        product_id,
        "SELL",
        base_size=base_size,
        limit_price=limit_price,
        stop_trigger_price=stop_trigger_price,
        end_time=end_time,
        commission_rate=commission_rate,
        is_max=is_max,
        tradable_balance=tradable_balance,
        skip_fcm_risk_check=skip_fcm_risk_check,
        leverage=leverage,
        margin_type=margin_type,
        retail_portfolio_id=retail_portfolio_id,
        **kwargs,
    )
