import style from "./Editor.module.scss";
import {
	Button,
	CopyButton,
	ScrollArea,
	SegmentedControl,
	Space,
	TextInput,
} from "@mantine/core";
import { useEffect, useState } from "react";
import { arrayKey, tuppleKey, useKeyPress } from "utils/utils";

const Editor: React.FC = () => {
	const [focused, setFocused] = useState(false);
	const [value, setValue] = useState("");
	const [code] = useKeyPress();
	return (
		<div className={style.editor}>
			<Space h="md" />
			<SegmentedControl
				className={style.radio}
				fullWidth={false}
				size={"lg"}
				data={[
					{ label: "macOS", value: "macOS" },
					{ label: "Windows", value: "Windows" },
				]}
			/>
			<Space h="md" />
			<TextInput
				className={style.input}
				label="Floating label"
				placeholder="OMG, it also has a placeholder"
				required
				value={value}
				onChange={(event) => setValue(event.currentTarget.value)}
				onFocus={() => setFocused(true)}
				onBlur={() => setFocused(false)}
				mt="md"
				autoComplete="nope"
			/>
			<Space h="md" />
			<ScrollArea style={{ height: 250 }}>
				{`key_output = (`}
				{<br />}
				{code}
				<br />
				{`)`}
			</ScrollArea>
			<Space h="md" />
			<CopyButton value="https://mantine.dev">
				{({ copied, copy }) => (
					<Button color={copied ? "teal" : "blue"} onClick={copy}>
						{copied ? "Copied url" : "Copy url"}
					</Button>
				)}
			</CopyButton>
			<Space h="md" />
		</div>
	);
};

export default Editor;
