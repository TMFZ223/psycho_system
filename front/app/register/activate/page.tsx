"use client";

import { useEffect, useState } from "react";
import { useRouter } from "next/navigation";

export default function ActivatePage() {
    useEffect(() => {
        document.title = "Страница регистрации";
    }, []);

    const router = useRouter();

    const [code, setCode] = useState("");

    const [error, setError] = useState("");

    const [success, setSuccess] = useState("");

    const handleActivate = async () => {

        try {

            const response = await fetch(
                `${process.env.NEXT_PUBLIC_BASE_URL_TEST_STAGE}/user/activate`,
                {
                    method: "POST",

                    headers: {
                        "Content-Type": "application/json",
                    },

                    body: JSON.stringify({
                        activation_code: code,
                    }),
                }
            );

            const result = await response.json();

            if (!result.success) {

                setError("введён неверный код");

                return;
            }

            setSuccess("успешная регистрация");

            setTimeout(() => {

                router.push("/login");

            }, 10000);

        } catch (error) {

            console.error(error);

            setError("Ошибка сервера");
        }
    };

    return (

        <div className="min-h-screen flex items-center justify-center bg-gray-100">

            <div className="bg-white p-8 rounded-2xl shadow-xl w-full max-w-md">

                <h1 className="text-2xl font-bold mb-8 text-center">
                    Введите код подтверждения,
                    отправленный на email
                </h1>

                {error && (
                    <div className="mb-4 bg-red-100 border border-red-400 text-red-700 p-3 rounded-lg">
                        {error}
                    </div>
                )}

                {success && (
                    <div className="mb-4 bg-green-100 border border-green-400 text-green-700 p-3 rounded-lg">
                        {success}
                    </div>
                )}

                <input
                    id="activation-code"
                    type="text"

                    value={code}

                    onChange={(e) => {

                        setCode(e.target.value);

                        setError("");
                    }}

                    placeholder="Код активации"

                    className="
                        w-full
                        border
                        border-gray-300
                        rounded-lg
                        p-3
                        mb-6
                    "
                />

                <button
                    id="send_code"
                    onClick={handleActivate}

                    disabled={!code.trim()}

                    className="
                        w-full
                        bg-blue-600
                        text-white
                        p-3
                        rounded-lg
                        disabled:opacity-50
                    "
                >
                    отправить
                </button>

            </div>
        </div>
    );
}