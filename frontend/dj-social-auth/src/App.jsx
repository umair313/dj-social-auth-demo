import {useState} from 'react'
import {ToastContainer, toast} from 'react-toastify';
import './App.css'
import FacebookLogin from 'react-facebook-login';
import 'react-toastify/dist/ReactToastify.css';
import {GoogleOAuthProvider, GoogleLogin, useGoogleLogin} from '@react-oauth/google';
import LoginWithGoogle from './google_login.jsx';

function App() {

    const flogin = (response) => {
        const myHeaders = new Headers();

        const formdata = new FormData();
        formdata.append("access_token", response?.accessToken);

        const requestOptions = {
            method: "POST",
            headers: myHeaders,
            body: formdata,
            redirect: "follow"
        };

        fetch("http://localhost:8000/users/facebook-login/", requestOptions)
            .then((response) => response.text())
            .then((result) => {
                toast(`Login as ${response?.name} 🚀`)
                console.log(result)
            })
            .catch((error) => {
                toast("Failed to login from local server. check console");
                console.error(error);
            });
    }

    const glogin = (response) => {
        const myHeaders = new Headers();

        const formdata = new FormData();
        formdata.append("access_token", response?.credential);

        const requestOptions = {
            method: "POST",
            headers: myHeaders,
            body: formdata,
            redirect: "follow"
        };

        fetch("http://localhost:8000/users/facebook-login/", requestOptions)
            .then((response) => response.text())
            .then((result) => {
                toast(`Login as ${response?.name} 🚀`)
                console.log(result)
            })
            .catch((error) => {
                toast("Failed to login from local server. check console");
                console.error(error);
            });
    }
    const responseFacebook = (response) => {
        console.log(response);
        if (response?.accessToken) {
            flogin(response)
        } else {
            toast("Failed from facebook. Check console!")
        }

    }
    const FACEBOOK_APP_ID = import.meta.env.VITE_FACEBOOK_APP_ID
    const GOOGLE_CLIENT_ID = import.meta.env.VITE_GOOGLE_CLIENT_ID

    return (
        <GoogleOAuthProvider clientId={GOOGLE_CLIENT_ID}>
            <div>
                <FacebookLogin
                    appId={FACEBOOK_APP_ID}
                    autoLoad={true}
                    fields="name,email,picture"
                    callback={responseFacebook}/>
                {/*Uncomment bellow component for code type flow */}
                {/*<LoginWithGoogle />*/}
                <GoogleLogin
                    onSuccess={credentialResponse => {
                        glogin(credentialResponse);
                    }}
                    onError={() => {
                        console.log('Login Failed');
                    }}
                />;
                <ToastContainer position="top-right"/>
            </div>
        </GoogleOAuthProvider>
    )
}

export default App;
