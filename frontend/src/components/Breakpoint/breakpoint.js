import React from "react";
import MediaQuery from "react-responsive";
const breakpoints = {
 desktop: "(min-width: 1000px)",
 tablet: "(min-width: 565px) and (max-width: 999px)",
 phone: "(max-width: 999px)",
};

//const { string, object } = React.PropTypes;

export default function Breakpoint(props) {
 const breakpoint = breakpoints[props.name] || breakpoints.desktop;

return (
    <MediaQuery {...props} query={breakpoint}>
        {props.children}
    </MediaQuery>
    );
}

