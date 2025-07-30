// src/components/SimulationSetup.tsx

import { useState } from "react";

interface Props {
    onCreateGrid: (robots: number, trash: number) => void;
}

export default function SimulationSetup({ onCreateGrid }: Props) {
    const [robots, setRobots] = useState(5);
    const [trash, setTrash] = useState(20);

    return (
        <div className="space-y-2">
            <h2 className="text-xl font-semibold">Configurer la simulation</h2>
            <div className="flex gap-4">
                <label>
                    Robots:
                    <input
                        type="number"
                        value={robots}
                        min={1}
                        onChange={(e) => setRobots(Number(e.target.value))}
                        className="ml-2 border px-2 py-1 rounded"
                    />
                </label>
                <label>
                    Déchets:
                    <input
                        type="number"
                        value={trash}
                        min={1}
                        onChange={(e) => setTrash(Number(e.target.value))}
                        className="ml-2 border px-2 py-1 rounded"
                    />
                </label>
            </div>
            <button
                onClick={() => onCreateGrid(robots, trash)}
                className="mt-2 px-4 py-2 bg-blue-500 text-white rounded hover:bg-blue-600"
            >
                Créer la grille
            </button>
        </div>
    );
}
