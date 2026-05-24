"use client";

import { useEffect, useState } from "react";
import { useRouter } from "next/navigation";

export default function RegisterPage() {
    useEffect(() => {
        document.title = "Страница регистрации";
    }, []);

    const router = useRouter();

    const [email, setEmail] = useState("");

    const [password, setPassword] = useState("");

    const [verifyPassword, setVerifyPassword] = useState("");

    const [emailError, setEmailError] = useState("");

    const [passwordError, setPasswordError] = useState("");

    const [verifyPasswordError, setVerifyPasswordError] = useState("");

    const [serverError, setServerError] = useState("");

    const validateEmail = (email: string) => {

        const emailRegex =
            /^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$/;

        return emailRegex.test(email);
    };

    const validatePassword = (password: string) => {

        if (password.length < 7 || password.length > 30) {
            return "Пароль должен быть не короче 7 и не длиннее 30 символов";
        }

        if (/[а-яА-Я\s]/.test(password)) {
            return "Некорректный формат пароля";
        }

        return "";
    };

    const validateFields = () => {

        let valid = true;

        setEmailError("");
        setPasswordError("");
        setVerifyPasswordError("");
        setServerError("");

        // EMAIL

        if (!email.trim()) {

            setEmailError("Обязательно для заполнения");

            valid = false;

        } else if (!validateEmail(email)) {

            setEmailError("Некорректный формат email");

            valid = false;
        }

        // PASSWORD

        if (!password.trim()) {

            setPasswordError("Обязательно для заполнения");

            valid = false;

        } else {

            const passwordValidation = validatePassword(password);

            if (passwordValidation) {

                setPasswordError(passwordValidation);

                valid = false;
            }
        }

        // VERIFY PASSWORD

        if (!verifyPassword.trim()) {

            setVerifyPasswordError("Обязательно для заполнения");

            valid = false;

        } else if (password !== verifyPassword) {

            setVerifyPasswordError("Пароли не совпадают");

            valid = false;
        }

        return valid;
    };

    const handleRegister = async () => {

        const isValid = validateFields();

        if (!isValid) {
            return;
        }

        try {

            const response = await fetch(
                `${process.env.NEXT_PUBLIC_BASE_URL_TEST_STAGE}/user/register`,
                {
                    method: "POST",

                    headers: {
                        "Content-Type": "application/json",
                    },

                    body: JSON.stringify({
                        email,
                        password,
                        verify_password: verifyPassword,
                    }),
                }
            );

            const result = await response.json();

            if (!result.success) {

                setServerError(
                    result.data.error_message
                );

                return;
            }

            localStorage.setItem(
                "activation_email",
                email
            );

            router.push("/register/activate");

        } catch (error) {

            console.error(error);

            setServerError("Ошибка сервера");
        }
    };

    return (

        <div className="min-h-screen bg-gray-100 flex items-center justify-center">

            <div className="bg-white p-8 rounded-2xl shadow-xl w-full max-w-md">

                <h1 className="text-3xl font-bold mb-8 text-center">
                    Регистрация пользователя
                </h1>

                {serverError && (
                    <div className="mb-4 bg-red-100 border border-red-400 text-red-700 p-3 rounded-lg">
                        {serverError}
                    </div>
                )}

                {/* EMAIL */}

                <div className="mb-4">

                    <label className="block mb-2">
                        Email
                    </label>

                    <input
                        id="email"
                        type="text"

                        value={email}

                        onChange={(e) => {

                            setEmail(e.target.value);

                            setEmailError("");
                        }}

                        className={`
                            w-full p-3 rounded-lg border
                            ${
                                emailError
                                    ? "border-red-500"
                                    : "border-gray-300"
                            }
                        `}
                    />

                    {emailError && (
                        <p className="text-red-500 text-sm mt-1">
                            {emailError}
                        </p>
                    )}
                </div>

                {/* PASSWORD */}

                <div className="mb-4">

                    <label className="block mb-2">
                        Пароль
                    </label>

                    <input
                        id="pass"
                        type="password"

                        value={password}

                        onChange={(e) => {

                            setPassword(e.target.value);

                            setPasswordError("");
                        }}

                        className={`
                            w-full p-3 rounded-lg border
                            ${
                                passwordError
                                    ? "border-red-500"
                                    : "border-gray-300"
                            }
                        `}
                    />

                    {passwordError && (
                        <p className="text-red-500 text-sm mt-1">
                            {passwordError}
                        </p>
                    )}
                </div>

                {/* VERIFY PASSWORD */}

                <div className="mb-6">

                    <label className="block mb-2">
                        Подтверждение пароля
                    </label>

                    <input
                        id="verify_pass"
                        type="password"

                        value={verifyPassword}

                        onChange={(e) => {

                            setVerifyPassword(
                                e.target.value
                            );

                            setVerifyPasswordError("");
                        }}

                        className={`
                            w-full p-3 rounded-lg border
                            ${
                                verifyPasswordError
                                    ? "border-red-500"
                                    : "border-gray-300"
                            }
                        `}
                    />

                    {verifyPasswordError && (
                        <p className="text-red-500 text-sm mt-1">
                            {verifyPasswordError}
                        </p>
                    )}
                </div>

                <button
                    id="register-BTN"
                    onClick={handleRegister}
                    className="
                        w-full
                        bg-blue-600
                        hover:bg-blue-700
                        text-white
                        p-3
                        rounded-lg
                        transition
                        mb-6
                    "
                >
                    Регистрация
                </button>

                <div className="text-center">

                    <p className="mb-3 text-gray-600">
                        Уже есть учётная запись?
                    </p>

                    <button
                        id="go_to_login_page"
                        onClick={() => router.push("/login")}
                        className="
                            text-blue-600
                            hover:underline
                        "
                    >
                        Войти
                    </button>

                </div>

            </div>
        </div>
    );
}