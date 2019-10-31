package dbshackathon.testlogin;

import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.*;

import javax.servlet.http.HttpServletResponse;
import java.io.IOException;
import java.util.HashMap;
import java.util.Map;

@RestController
public class WebController {

//    @RequestMapping(value = "/", method = RequestMethod.GET)
//    void redirect(HttpServletResponse response) throws IOException {
//        response.sendRedirect("/login");
//    }
//
//    @RequestMapping(value = "/login", method = RequestMethod.GET)
//    public String login() {
//        return "login";
//    }

    @RequestMapping("/")
    public String index() {
        return "Greetings from Level up lunch!";
    }

    @RequestMapping("/jsontest")
    public @ResponseBody Map<String, String> callSomething () {

        Map<String, String> map = new HashMap<String, String>();
        map.put("url", "http://www.leveluplunch.com");

        return map;
    }

}