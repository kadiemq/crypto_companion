import React, {useEffect, useState} from "react";
import './style.css'
import {useC} from "../utils/context";
import axios from "axios";
import {Link} from "react-router-dom";

const AlertsPage = () => {

    const {loading, systemMsg} = useC()

    const [loadingValue, setLoading] = loading
    const [, setSystemMsg] = systemMsg

    const [alerts, setAlerts] = useState([])

    const handle_delete = (e) => {
        e.preventDefault();

        const id = e.target.id

        setLoading(true);
        axios.delete(``, {withCredentials: true})
            .then((r) => {
                const new_array = alerts.filter((a) => {
                    return a.id === id
                })
                setAlerts(new_array)
                setSystemMsg('Alert Deleted')
                setLoading(false);
            })
            .catch((e) => {
                setLoading(false);
                console.log(e)
            })
    }

    useEffect(() => {
        setLoading(true);
        axios.get('', {withCredentials: true})
            .then((r) => {
                setAlerts(r.data)
                setLoading(false);
            })
            .catch((e) => {
                setLoading(false);
                console.log(e)
            })

    }, [])

    if(loadingValue) {
        return ''
    }

    return (
        <section className={'alerts_section'}>

            <div className="alerts_add_news_wrapper">
                <Link to={'/new_alert'}>Add new alert</Link>
            </div>

            <div className="alerts_wrapper">
                {alerts.map((alert, idx) => {
                    return (
                        <div className={'alert_single'} key={idx}>

                            <div className="alert_symbol">
                                <p>{alert.symbol}</p>
                            </div>

                            <div className="alert_info">
                                <p>{alert.direction}</p>
                                <p>{alert.trigger}</p>
                                <p>{alert.message}</p>
                            </div>

                            <div className="alert_actions">
                                <button id={alert.id} onClick={handle_delete}>Delete</button>
                            </div>

                        </div>
                    )
                })}
            </div>

        </section>
    )
}

export default AlertsPage;
