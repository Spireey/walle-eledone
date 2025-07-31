interface Props {
    simulationStarted: boolean;
    onStart: () => void;
    onReset: () => void;
}

export default function Controls({ simulationStarted, onStart, onReset }: Props) {
    return (
        <div className="flex gap-4 mt-4">
            {!simulationStarted && (
                <button
                    onClick={onStart}
                    className="px-4 py-2 bg-green-500 text-white rounded hover:bg-green-600"
                >
                    Start Simulation
                </button>
            )}
            <button
                onClick={onReset}
                className="px-4 py-2 bg-red-500 text-white rounded hover:bg-red-600"
            >
                Reset Simulation
            </button>
        </div>
    );
}
