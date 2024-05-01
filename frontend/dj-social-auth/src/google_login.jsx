import {useGoogleLogin} from '@react-oauth/google';

export default function LoginWithGoogle(){
    const GoogleLoginBackend = useGoogleLogin({
      onSuccess: codeResponse => console.log(codeResponse),
      flow: 'auth-code',
    });
    return (
        <>
            <button
                onClick={() => GoogleLoginBackend()}
            >Login with Google
            </button>
        </>
    )
}
