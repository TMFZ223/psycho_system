"use client";

import { useEffect, useState } from "react";
import { useRouter } from "next/navigation";

type User = {
    email: string;
    role: string;
    access_token: string;
};

export default function DashboardPage() {

    const router = useRouter();

    const [user, setUser] = useState<User | null>(null);

    const [profileOpen, setProfileOpen] =
        useState(false);

    const [modulesOpen, setModulesOpen] =
        useState(false);

    const roleLabels: Record<string, string> = {
        admin: "Преподаватель",
        user: "Ученик",
    };

    useEffect(() => {

        document.title = "Главная";

        const storedUser =
            localStorage.getItem("user");

        if (!storedUser) {

            router.push("/login");

            return;
        }

        setUser(
            JSON.parse(storedUser)
        );

    }, [router]);

    const logout = () => {

        localStorage.removeItem("user");

        router.push("/login");
    };

    if (!user) {
        return null;
    }

    return (

        <div className="min-h-screen bg-gray-100">

            {/* HEADER */}

            <header
                className="
                    bg-white
                    shadow
                    px-6
                    py-4
                    flex
                    justify-between
                    items-center
                "
            >

                <h1
                    className="
                        text-2xl
                        font-bold
                    "
                >
                    Главная страница
                </h1>

                <div
                    className="
                        flex
                        items-center
                        gap-4
                    "
                >

                    {/* СПИСОК МОДУЛЕЙ */}

                    <div className="relative">

                        <button
                            id="modules-BTN"
                            onClick={() =>
                                setModulesOpen(
                                    !modulesOpen
                                )
                            }
                            className="
                                bg-blue-600
                                text-white
                                px-4
                                py-2
                                rounded
                            "
                        >
                            Список модулей
                        </button>

                        {modulesOpen && (

                            <div
                                className="
                                    absolute
                                    left-0
                                    mt-2
                                    bg-white
                                    border
                                    rounded
                                    shadow
                                    w-48
                                    z-10
                                "
                            >

                                <button
                                    onClick={() =>
                                        router.push(
                                            "/modules/module1"
                                        )
                                    }
                                    className="
                                        block
                                        w-full
                                        text-left
                                        px-4
                                        py-2
                                        hover:bg-gray-100
                                    "
                                >
                                    Опросник для подростков 12-18 лет
                                </button>

                            </div>

                        )}

                    </div>

                    {/* ТОЛЬКО ДЛЯ ADMIN */}

                    {user.role === "admin" && (

                        <button
                            onClick={() =>
                                router.push(
                                    "/users"
                                )
                            }
                            className="
                                text-blue-600
                                hover:underline
                            "
                        >
                            Список пользователей
                        </button>

                    )}

                    {/* ПРОФИЛЬ */}

                    <div className="relative">

                        <button
                            id="profile-BTN"
                            onClick={() =>
                                setProfileOpen(
                                    !profileOpen
                                )
                            }
                            className="
                                bg-green-600
                                text-white
                                px-4
                                py-2
                                rounded
                            "
                        >
                            Профиль
                        </button>

                        {profileOpen && (

                            <div
                                className="
                                    absolute
                                    right-0
                                    mt-2
                                    w-72
                                    bg-white
                                    border
                                    rounded-lg
                                    shadow-lg
                                    p-4
                                    z-10
                                "
                            >

                                <div
                                    id="user-role"
                                    className="
                                        text-sm
                                        text-gray-500
                                        mb-4
                                    "
                                >
                                    Роль:
                                    {" "}
                                    {
                                        roleLabels[
                                            user.role
                                        ] ||
                                        "Неизвестна"
                                    }
                                </div>

                                <button
                                    onClick={
                                        logout
                                    }
                                    className="
                                        text-red-500
                                        hover:underline
                                    "
                                >
                                    Выйти
                                </button>

                            </div>

                        )}

                    </div>

                </div>

            </header>

            {/* CONTENT */}

            <main className="p-6">

                <div
                    className="
                        bg-white
                        rounded-lg
                        shadow
                        p-6
                    "
                >

                    <h2
                        className="
                            text-xl
                            font-semibold
                            mb-2
                        "
                    >
                        Добро пожаловать
                    </h2>

                    <p>
                        Выберите модуль
                        через меню сверху.
                    </p>

                </div>

            </main>

        </div>

    );
}