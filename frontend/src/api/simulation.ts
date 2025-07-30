import axios from "axios";
import type { SimulationState } from "../types/simulation";

axios.defaults.baseURL = "http://localhost:8000";

export const createGrid = (robots: number, trash: number) => {
    return axios.post<SimulationState>("/create_grid", { robots, trash }).then(res => res.data);
};

export const startSimulation = () => {
    return axios.post("/start_simulation");
};

export const stepSimulation = () => {
    return axios.post("/step_simulation");
};

export const resetSimulation = () => {
    return axios.post("/reset_simulation");
};

export const getSimulationState = () => {
    return axios.get<SimulationState>("/get_state").then(res => res.data);
};
