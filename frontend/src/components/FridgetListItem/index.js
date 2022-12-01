import * as React from "react";
import List from "@mui/material/List";
import ListItem from "@mui/material/ListItem";
import ListItemButton from "@mui/material/ListItemButton";
import ListItemIcon from "@mui/material/ListItemIcon";
import ListItemText from "@mui/material/ListItemText";
import Checkbox from "@mui/material/Checkbox";
import IconButton from "@mui/material/IconButton";
import DeleteIcon from "@mui/icons-material/Delete";
import AddIcon from "@mui/icons-material/Add";
import { Input } from "@mui/material";
import axios from "axios";
import { useNavigate } from "react-router-dom";
import {
  routes,
  getUserIngredients,
  addUserIngredients,
  AppContext,
  API_URL,
} from "../../constants";
import styles from "./styles.css";

/**
 * This function is a React component that renders a list of items in the "fridget". It also allows the
 * user to add new items to the list
 * @returns A list of items in the fridge.
 */
export default function FridgetListItem() {
  const { checked, setChecked } = React.useContext(AppContext);
  const [fridgetItems, setFridgetItems] = React.useState([]);
  const [newFridgetItem, setNewFridgetItem] = React.useState(null);
  const navigate = useNavigate();

  const getFridgetItems = () => {
    axios({
      method: "get",
      url: API_URL + getUserIngredients,
      headers: { "Content-Type": "application/json" },
      body: {},
    })
      .then((response) => {
        setFridgetItems(response.data?.ingredients);
      })
      .catch((error) => {
        console.log(error);
        localStorage.setItem("auth", false);
        navigate(routes.home);
      });
  };

  const addFridgetItem = () => {
    if (newFridgetItem) {
      axios({
        method: "post",
        url: API_URL + addUserIngredients,
        headers: { "Content-Type": "application/json" },
        data: {
          ingredients: [newFridgetItem],
        },
      });
      getFridgetItems();
    }
  };

  React.useEffect(() => {
    getFridgetItems();
  }, []);

  const handleToggle = (value) => () => {
    const currentIndex = checked.indexOf(value);
    const newChecked = [...checked];

    if (currentIndex === -1) {
      newChecked.push(value);
    } else {
      newChecked.splice(currentIndex, 1);
    }

    setChecked(newChecked);
  };

  return (
    <List lg={{ width: "100%", maxWidth: 360, bgcolor: "background.paper" }}>
      {fridgetItems?.map((value) => {
        const labelId = `checkbox-list-label-${value}`;

        return (
          <ListItem
            key={value}
            secondaryAction={
              <IconButton edge="end" aria-label="delete">
                <DeleteIcon />
              </IconButton>
            }
            disablePadding
          >
            <ListItemButton
              role={undefined}
              onClick={handleToggle(value)}
              dense
            >
              <ListItemIcon>
                <Checkbox
                  edge="start"
                  checked={checked.indexOf(value) !== -1}
                  tabIndex={-1}
                  disableRipple
                  inputProps={{ "aria-labelledby": labelId }}
                />
              </ListItemIcon>
              <ListItemText id={labelId} primary={`${value}`} />
            </ListItemButton>
          </ListItem>
        );
      })}
      <ListItem disablePadding>
        <ListItemButton onClick={addFridgetItem} role={undefined} dense>
          <ListItemIcon>
            <AddIcon />
          </ListItemIcon>
          <Input
            value={newFridgetItem}
            onChange={(e) => setNewFridgetItem(e.target.value)}
            className="add-item"
          />
        </ListItemButton>
      </ListItem>
    </List>
  );
}
