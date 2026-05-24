"use client";
import { useEffect, useState } from "react";

export default function DashboardPage() {
    const [user, setUser] = useState<any>(null);
    const [profileOpen, setProfileOpen] = useState(false);
const roleLabels: Record<string, string> = {
    admin: "Преподаватель",
    user: "Ученик",
};

    useEffect(() => {
        document.title = "Главная";
        const storedUser = localStorage.getItem("user");

        if (!storedUser) {
            window.location.href = "/login";
            return;
        }

        setUser(JSON.parse(storedUser));
    }, []);

    const logout = () => {
        localStorage.removeItem("user");
        window.location.href = "/login";
    };

    if (!user) return null;

    return (
        <div className="min-h-screen bg-gray-100">

            {/* HEADER */}
            <header className="bg-white shadow p-4 flex justify-between items-center">
                <h1 className="text-2xl font-bold">
                    Главная страница
                </h1>

                <div className="relative">
                    <button
                        id="profile-BTN"
                        onClick={() => setProfileOpen(!profileOpen)}
                        className="w-10 h-10 rounded-full bg-blue-500 text-white"
                    >
                        Профиль
                    </button>

                    {profileOpen && (
                        <div className="absolute right-0 mt-2 w-64 bg-white border rounded-lg shadow-lg p-4">
                            <p id="user-role" className="text-sm text-gray-500 mb-4">
                                Роль пользователя: {roleLabels[user.role] || "Неизвестна"}
                            </p>

                            <button
                                onClick={logout}
                                className="text-red-500 hover:underline"
                            >
                                выйти
                            </button>
                        </div>
                    )}
                </div>
            </header>

            {/* CONTENT */}
            <main className="p-6">

                {/* MENU */}
                <div className="mb-6">
                    <h2 className="text-xl font-semibold mb-2">
                        Меню
                    </h2>

                    <ul className="space-y-2">
                        <li className="bg-white p-4 rounded-lg shadow">
                            Список тестовых заданий
                        </li>

                        {user.role === "admin" && (
                            <li className="bg-white p-4 rounded-lg shadow">
                                Список зарегистрированных пользователей
                            </li>
                        )}
                    </ul>
                </div>
            </main>
        </div>
    );
}