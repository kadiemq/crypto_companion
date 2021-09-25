import {Redirect, Route} from "react-router-dom";
import {useC} from "./context";
import React from "react";

export default function AuthenticatedAndHaveApiRoute({ children, ...rest }) {

    const {isAuthenticated, haveApi} = useC()
    const [isAuthenticatedValue] = isAuthenticated
    const [haveApiValue] = haveApi
    return (
        <Route
            {...rest}
            render={({ location }) =>
                (isAuthenticatedValue && haveApiValue) ? (
                    children
                ) : (
                    <Redirect
                        to={{
                            pathname: "/login",
                            state: { from: location }
                        }}
                    />
                )
            }
        />
    )
}
