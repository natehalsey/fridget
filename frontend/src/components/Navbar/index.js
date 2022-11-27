import { Nav, NavLink, Bars, NavMenu, NavBtn } from "./NavbarElements";

const Navbar = () => {
  return (
    <div>
      <Nav>
        <Bars />

        <NavMenu>
        <NavLink to="/home" >
            Home
          </NavLink>
          <NavLink to="/about" >
            About
          </NavLink>
          <NavLink to="/api" >
            API
          </NavLink>
        </NavMenu>
      </Nav>
    </div>
  );
};

export default Navbar;
