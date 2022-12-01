import "./Pages.css";
import "@lottiefiles/lottie-player";

/**
 * This function renders the About page, which contains a brief description of the Fridget app, as well
 * as the mission statement
 * @returns A React component
 */
const About = () => {
  return (
    <div className="About">
      <div className="container out">
        <div className="row">
          <div className="col-xs-12 col-sm-7 ">
            <h4 className="visionh2">About Us</h4>
            <p className="list-group d-flex justify-content-start">
              Over a third of all food produced (~2.5 billion tons) is lost or
              wasted each year. Fridget aims to get this number down by
              encouraging users to cook what's in their fridge. So don't eat out
              tonight, fridget instead. Or, use our platform to share recipes
              with your friends and family, easily and seamlessly.
            </p>
          </div>
          <div className="col-xs-12 col-sm-5 vimg d-flex justify-content-center">
            <lottie-player
              src="https://assets1.lottiefiles.com/packages/lf20_6efbhc0k.json"
              background="transparent"
              speed={1}
              style={{ width: "300px", height: "300px" }}
              loop
              autoPlay
            />
          </div>
        </div>
        <div className="row">
          <div className="col-xs-12 col-sm-7">
            <h4 className="missionh2 d-flex justify-content-end text-secondary">
              Mission
            </h4>
            <p className="list-group d-flex justify-content-start ">
              It's our mission to provide a free and safe platform for
              individuals to easily share and manage their recipes, manage their
              fridge ingredients, and find recipes they can make right now --
              with just the items in their fridge.
            </p>
          </div>
          <div className="col-sm-5 hidden-xs d-flex justify-content-center vimg mimg">
            <lottie-player
              src="https://assets1.lottiefiles.com/packages/lf20_jbt4j3ea.json"
              background="transparent"
              speed={1}
              style={{ width: "300px", height: "300px" }}
              loop
              autoPlay
            />
          </div>
        </div>
      </div>
    </div>
  );
};
export default About;
