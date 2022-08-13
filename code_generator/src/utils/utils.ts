import { useCallback, useEffect, useState } from "react";

export const useKeyPress = () => {
	const [key, setKey] = useState("");
	const handleUserKeyPress = useCallback((event: any) => {
		const { code, key, keyCode } = event;
		console.log(key, keyCode);
		console.log(event);

		// if(entrr && typetex) {

		// }
		if (code in tuppleKey) {
			console.log("special key");
			return;
		}

		if (code in arrayKey) {
			console.log(arrayKey[key]);
			return;
		}

		setKey((prevCode: any) => prevCode + key);
	}, []);

	useEffect(() => {
		window.addEventListener("keydown", handleUserKeyPress);
		return () => {
			window.removeEventListener("keydown", handleUserKeyPress);
		};
	}, [handleUserKeyPress]);
	return [key];
};

// export default useKeyPress;

export const tuppleKey: any = {
	ShiftLeft: "d",
	ShiftRight: "d",
	MetaLeft: "d",
	MetaRight: "d",
	ControlLeft: "d",
	ControlRight: "d",
	AltLeft: "d",
	AltRight: "d",
};

export const arrayKey: any = {
	Enter: "d",
	ArrowDown: "d",
	ArrowUp: "d",
	ArrowRight: "d",
	ArrowLeft: "d",
	Space: "d",
};
