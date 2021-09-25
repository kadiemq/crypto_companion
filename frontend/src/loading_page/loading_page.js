import React from "react";
import './style.css'
import logo from '../logo.png'
import {useC} from "../utils/context";

const LoadingPage = () => {
    const {loading} = useC()
    const [loadingValue] = loading

    if (!loadingValue) {
        return '';
    }
    return (
        <section className={'loading_page_section'}>
            <div className={'loading_page_wrapper'}>
                <div className={'logo_div'}>
                    <img src={logo} alt={'logo'}/>
                </div>

                <div className={'loading_div'}>
                    <p>Loading</p>
                </div>
            </div>
        </section>
    )
}

export default LoadingPage
