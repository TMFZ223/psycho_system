"use client";

import { useEffect, useState } from "react";
import { useRouter } from "next/navigation";

export default function LoginPage() {
    useEffect(() => {
        document.title = "Система диагностики посттравматического расстройства незрячих людей";
    }, []);

    const router = useRouter();

    const [email, setEmail] = useState("");
    const [password, setPassword] = useState("");

    const [emailError, setEmailError] = useState("");
    const [passwordError, setPasswordError] = useState("");

    const [authError, setAuthError] = useState("");
    const [loading, setLoading] = useState(false);

    const validateFields = () => {
        let valid = true;

        if (!email.trim()) {
            setEmailError("Обязательно для заполнения");
            valid = false;
        } else {
            setEmailError("");
        }

        if (!password.trim()) {
            setPasswordError("Обязательно для заполнения");
            valid = false;
        } else {
            setPasswordError("");
        }

        return valid;
    };

    const handleLogin = async () => {
        setAuthError("");

        const isValid = validateFields();

        if (!isValid) {
            return;
        }

        try {
            setLoading(true);

            const response = await fetch(
                `${process.env.NEXT_PUBLIC_BASE_URL_TEST_STAGE}/user/auth`,
                {
                    method: "POST",

                    headers: {
                        "Content-Type": "application/json",
                    },

                    body: JSON.stringify({
                        email,
                        password,
                    }),
                }
            );

            const result = await response.json();

            if (!result.success) {
                setAuthError("вы ввели неверные данные");
                return;
            }

            localStorage.setItem(
                "user",
                JSON.stringify({
                    role: result.data.role,
                    access_token: result.data.access_token,
                    refresh_token: result.data.refresh_token,
                })
            );

            router.push("/dashboard");

        } catch (error) {
            console.error(error);

            setAuthError("Ошибка сервера");

        } finally {
            setLoading(false);
        }
    };

    return (
        <div className="min-h-screen bg-gray-100 flex items-center justify-center">

            <div className="w-full max-w-md bg-white rounded-2xl shadow-xl p-8">

                {/* Ошибка авторизации */}
                {authError && (
                    <div className="mb-4 rounded-lg bg-red-100 border border-red-400 p-3 text-red-700">
                        {authError}
                    </div>
                )}

                {/* Заголовок */}
                <h1 className="text-3xl font-bold mb-8 text-center">
                    вход
                </h1>

                {/* EMAIL */}
                <div className="mb-5">
                    <label className="block mb-2 text-sm font-medium">
                        Email
                    </label>

                    <input
                        id="email"
                        type="text"
                        placeholder="email"
                        value={email}
                        onChange={(e) => {
                            setEmail(e.target.value);

                            if (e.target.value.trim()) {
                                setEmailError("");
                            }
                        }}
                        className={`
                            w-full
                            rounded-lg
                            border
                            p-3
                            outline-none
                            transition
                            ${
                                emailError
                                    ? "border-red-500"
                                    : "border-gray-300"
                            }
                        `}
                    />

                    {emailError && (
                        <p className="mt-1 text-sm text-red-500">
                            {emailError}
                        </p>
                    )}
                </div>

                {/* PASSWORD */}
                <div className="mb-6">
                    <label className="block mb-2 text-sm font-medium">
                        Пароль
                    </label>

                    <input
                        id="pass"
                        type="password"
                        placeholder="пароль"
                        value={password}
                        onChange={(e) => {
                            setPassword(e.target.value);

                            if (e.target.value.trim()) {
                                setPasswordError("");
                            }
                        }}
                        className={`
                            w-full
                            rounded-lg
                            border
                            p-3
                            outline-none
                            transition
                            ${
                                passwordError
                                    ? "border-red-500"
                                    : "border-gray-300"
                            }
                        `}
                    />

                    {passwordError && (
                        <p className="mt-1 text-sm text-red-500">
                            {passwordError}
                        </p>
                    )}
                </div>

                {/* КНОПКИ */}
                <div className="flex flex-col gap-3">

                    <button
                        id="login-button"
                        onClick={handleLogin}
                        disabled={loading}
                        className="
                            bg-blue-600
                            text-white
                            rounded-lg
                            p-3
                            hover:bg-blue-700
                            transition
                            disabled:opacity-50
                        "
                    >
                        {loading ? "Загрузка..." : "Войти"}
                    </button>

                    <button
                        id="register"
                        onClick={() => router.push("/register")}
                        className="
                            border
                            border-gray-300
                            rounded-lg
                            p-3
                            hover:bg-gray-100
                            transition
                        "
                    >
                        Регистрация
                    </button>

                    <button
                        className="
                            text-blue-600
                            hover:underline
                            text-sm
                        "
                    >
                        Забыли пароль?
                    </button>

                </div>
            </div>
        </div>
    );
}