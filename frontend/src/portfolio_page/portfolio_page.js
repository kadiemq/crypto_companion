import React, {useState, useEffect} from "react";
import './style.css'
import {useC} from "../utils/context";
import {Redirect} from "react-router-dom";
import axios from "axios";

const PortfolioPage = () => {

    const {haveApi, loading} = useC()
    const [haveApiValue] = haveApi
    const [loadingValue, setLoading] = loading

    const [coinList, setCoinList] = useState([])
    const [networth, setNetworth] = useState(0)

    useEffect(() => {
        setLoading(true);
        axios.get('', {withCredentials: true})
            .then((r) => {
                setNetworth(r.data.estimated_net_worth)
                setCoinList(r.data.coin_list)
                setLoading(false);
            })
            .catch((e) => {
                setLoading(false);
                console.log(e)
            })

    }, [])

    if (!haveApiValue) {
        console.log('No Api')
        return <Redirect to="/binance_api" />
    }

    if(loadingValue) {
        return ''
    }

    return (
        <section className={'portfolio_section'}>
            <div className={'portfolio_networth_div'}>Estimated Networth: {networth.toFixed(2)}$</div>

            {coinList.map((coin, idx) => {
                if(!coin.symbol) return ''
                return (
                <div className={'portfolio_coin_wrapper'}>
                    <p>{coin.symbol}</p>
                    <p>Quantity: {parseFloat(coin.locked)+ parseFloat(coin.free)}</p>
                    <p>Current Price: {parseFloat(coin.current_price).toFixed(4)}$, Current Value: {parseFloat(coin.current_value).toFixed(2)}$</p>
                    <p>Cost Per Coin: {parseFloat(coin.cost_per_token).toFixed(4)}$, Original Value: {((parseFloat(coin.locked)+ parseFloat(coin.free)) * parseFloat(coin.cost_per_token)).toFixed(2)}$</p>
                    <p>Profit: {parseFloat(coin.profitability).toFixed(2)}$ ({parseFloat(coin.profitability_percentage*100).toFixed(2)}%)</p>
                </div>
            )})}
        </section>
    )
}

export default PortfolioPage;
