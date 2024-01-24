from brownie import FundMe, network, config, MockV3Aggregator
from scripts.helpful_scripts import get_account, deploy_mock3aggregator, LOCAL_BLOCKCHAIN_ENVIRONMENTS

def deploy_fund_me():
    account = get_account()

    if network.show_active() not in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        price_feed_address = config["networks"][network.show_active()]["eth_usd_price_feed"]
    else:
        deploy_mock3aggregator()
        price_feed_address = MockV3Aggregator[-1].address

    fund_me = FundMe.deploy(
        price_feed_address,
        {"from": account},
        publish_source=config["networks"][network.show_active()]["verify"]
    )
    print(f"contract deployed to {fund_me.address}")
    return fund_me

def main():
    deploy_fund_me()