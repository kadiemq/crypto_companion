import React, {useEffect, useState} from "react";
import './style.css'
import axios from "axios";
import {useC} from "../utils/context";

const NewsPage = () => {

    const {loading} = useC()
    const [loadingValue, setLoading] = loading

    const [news, setNews] = useState([])

    useEffect(() => {
        axios.get('')
            .then((r) => {
                setNews(r.data)
            })
            .catch((e) => console.log(e))
    }, [])

    if(news.length === 0) {
        setLoading(true);
        return ''
    } else {
        setLoading(false);
        return (
            <section className={'news_section'}>

                {news.map((article, idx) => {return(
                    <div className="news_article_div" key={idx}>

                        <div className="news_image_wrapper">
                            <img src={article.image} alt={'news_image'}/>
                        </div>

                        <div className={'news_title_wrapper'}>
                            <a href={article.url} target="_blank">{article.title}</a>
                        </div>

                    </div>
                )})}

            </section>
        )
    }
}

export default NewsPage;
