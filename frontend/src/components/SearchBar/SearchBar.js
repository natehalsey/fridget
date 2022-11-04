import React, { useState } from "react";
import styles from "./SearchBar.css";
import { Users } from "./Users";

const SearchBar = () => {
  const [query, setQuery] = useState("");

  return (
    <div className={styles.staticpage}>
      <input
        type="text"
        placeholder="Search..."
        className="search"
        onChange={(e) => setQuery(e.target.value)}
      />
      <ul className="list">
        {Users.filter((user) =>
          user.first_name.toLowerCase().includes(query.toLowerCase())
        ).map((user) => (
          <li key={user.id} className="listItem">
            {user.first_name}
          </li>
        ))}
      </ul>
    </div>
  );
};

export default SearchBar;
