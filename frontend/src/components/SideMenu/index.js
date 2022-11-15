import React from "react";
import Radio from '@mui/material/Radio';
import RadioGroup from '@mui/material/RadioGroup';
import FormControlLabel from '@mui/material/FormControlLabel';
import FormControl from '@mui/material/FormControl';
import Typography from '@mui/material/Typography';
import Paper from '@mui/material/Paper';
import Button from '@mui/material/Button';
import { searchParamArea, searchParamCategory, searchParamIngredient, searchParamName, AppContext } from "../../constants";
import styles from "./styles.css"

export default function SideMenu() {
    const {searchParams, setSearchParams, user } = React.useContext(AppContext);

    const handleChange = (event) => {
        setSearchParams(event.target.value);
    };

    return (
        <Paper className="sideMenu"> 
        <Typography gutterBottom variant="h5" component="div">
            Search Parameters
        </Typography>
            <FormControl>
                <RadioGroup
                    aria-labelledby="controlled-radio-buttons-group"
                    name="controlled-radio-buttons-group"
                    value={searchParams}
                    onChange={handleChange}
                >
                    <FormControlLabel value={searchParamName} control={<Radio />} label="Search By Name" />
                    <FormControlLabel value={searchParamArea} control={<Radio />} label="Search By Area" />
                    <FormControlLabel value={searchParamCategory} control={<Radio />} label="Search By Category" />
                    <FormControlLabel value={searchParamIngredient} control={<Radio />} label="Search By Ingredients" />
                </RadioGroup>
                </FormControl>
                {Object.keys(user).length !== 0 && ( 
                    <>
                    <Button className="createBtn" variant="contained" onClick={() => {window.location.href = `/create`}}>Create Recipe</Button>
                    <Button className="addBtn" variant="contained" onClick={() => {window.location.href = `/fridget`}}>Add Item to Fridget</Button>
                    </>
                )}
        </Paper>
    );
}