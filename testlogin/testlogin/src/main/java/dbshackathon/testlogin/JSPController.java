package dbshackathon.testlogin;

import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.servlet.ModelAndView;

@RestController
public class JSPController {

    @RequestMapping("/jsptest")
    public String test(ModelAndView modelAndView) {
        return "jsp-spring-boot";
    }

}