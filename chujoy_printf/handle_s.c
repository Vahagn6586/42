/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_print_str.c                                     :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: vrafyan <marvin@42.fr>                     +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/03/06 15:25:56 by vrafyan           #+#    #+#             */
/*   Updated: 2026/03/06 15:25:59 by vrafyan          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "ft_printf.h"

int	handle_s(va_list *arg)
{
	char	*ptr;

	ptr = va_arg(*arg, char *);
	if (!ptr)
	{
		ft_putstr("(null)");
		return (6);
	}
	ft_putstr(ptr);
	return (ft_strlen(ptr));
}
